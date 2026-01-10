from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

@app.route('/')
def show_form():
    return render_template("index.html")

@app.route('/analyze', methods = ['POST'])
def analyze():
    resume_file = request.files['resume']
    job_description = request.form["job_description"]

    return "recieved!"
   
if __name__ == "__main__":
    app.run(debug=True)

