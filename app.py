from flask import Flask, render_template, request, redirect, url_for
from analyzer.extract import extract_text_from_pdf
from analyzer.skills import load_taxonomy
app = Flask(__name__)

@app.route('/')
def show_form():
    return render_template("index.html")

@app.route('/analyze', methods = ['POST'])
def analyze():
    resume_file = request.files['resume']
    job_description = request.form["job_description"]
    resume_text = extract_text_from_pdf(resume_file)
    taxonomy = load_taxonomy()

    print("-------Resume Preview---------")
    print(resume_text[:300])
    print("------------------------------")

    return "recieved!"
   
if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)

