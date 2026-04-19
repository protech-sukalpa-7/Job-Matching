from flask import Flask, render_template, request
from predict import match_jobs

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    results = None

    if request.method == "POST":
        resume = request.form["resume"]
        results = match_jobs(resume)

    return render_template("index.html", results=results)

if __name__ == "__main__":
    app.run(debug=True)