from flask import Flask, render_template, request
from analyzer.extract import extract_text_from_pdf
from analyzer.preprocess import text_cleaning
from analyzer.skills import load_taxonomy, detect_skills
from analyzer.scoring import score_resume
from analyzer.feedback import generate_feedback
from analyzer.db import init_db,save_analysis,get_history
import json

app = Flask(__name__)
init_db()

@app.route('/')
def show_form():
    return render_template("index.html")

@app.route('/analyze', methods=['POST'])
def analyze():
    
    resume_file = request.files['resume']
    job_description = request.form['job_description']

   
    resume_text = extract_text_from_pdf(resume_file)

    
    taxonomy = load_taxonomy()

    
    resume_cleaned, resume_tokens = text_cleaning(resume_text)
    jd_cleaned, jd_tokens = text_cleaning(job_description)

   
    matched_skills_resume = detect_skills(
        resume_cleaned, resume_tokens, taxonomy
    )
    matched_skills_jd = detect_skills(
        jd_cleaned, jd_tokens, taxonomy
    )

    
    missing_skills = {}

    for category in taxonomy.keys():
        resume_set = set(matched_skills_resume.get(category, []))
        jd_set = set(matched_skills_jd.get(category, []))
        missing_skills[category] = list(jd_set - resume_set)

    
    print(f"Resume tokens: {len(resume_tokens)}")
    print(f"JD tokens: {len(jd_tokens)}")
    print("Missing skills:", missing_skills)

    score_breakdown = score_resume(matched_skills_resume,matched_skills_jd,resume_tokens,jd_tokens,resume_cleaned,taxonomy)
    feedback = generate_feedback(missing_skills,resume_cleaned)
    save_analysis(score =score_breakdown["final_score"],missing_skills=missing_skills)

    return render_template(
  "results.html",
  matched_skills_resume=matched_skills_resume,
  matched_skills_jd=matched_skills_jd,
  missing_skills=missing_skills,
  resume_token_count=len(resume_tokens),
  jd_token_count=len(jd_tokens),
  score_breakdown = score_breakdown,
  feedback = feedback
)

@app.route('/history')
def history():
    rows = get_history()

    history_items = []

    for row in rows:
        id, timestamp, score, missing_skills_json, job_title = row
        missing_skills = json.loads(missing_skills_json)

        history_items.append({
            "id": id,
            "timestamp": timestamp,
            "score": score,
            "missing_skills": missing_skills,
            "job_title": job_title
        })

    return render_template("history.html", history=history_items)



if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)
