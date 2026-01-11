# Resume Analyzer 📝

A full-stack Flask web application that analyzes a resume against a job description, identifies skill matches and gaps, provides improvement feedback, computes a match score, and stores analysis history using SQLite.


---

##  Features

- Upload a PDF resume (parsed using pdfplumber)
- Paste a job description
- Text preprocessing:
  - Lowercasing
  - Punctuation removal
  - Whitespace normalization
  - Tokenization
  - Stopword filtering
- Skill detection using a custom taxonomy:
  - Programming languages
  - Frameworks
  - Tools
  - Core concepts
- Resume–job matching score:
  - Skill match ratio
  - Keyword overlap
  - Resume section detection
- Human-readable improvement feedback
- Persistent analysis history using SQLite
- Clean, responsive UI with HTML, CSS, and Jinja templates

---

## 🧠 Tech Stack

- Backend: Python, Flask
- Frontend: HTML, CSS (Jinja templates)
- Database: SQLite
- Resume Parsing: pdfplumber
- Text Processing: Custom preprocessing logic


## ▶️ How to Run

```bash
pip install -r requirements.txt
python app.py




