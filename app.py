from flask import Flask, render_template, request
import pandas as pd

from ai_analyzer import analyze_answer
from score_manager import ScoreManager
from report_generator import save_report

app = Flask(__name__)

# Load dataset
df = pd.read_csv("dataset/interview_questions.csv")

score_manager = ScoreManager()


# Home Page
@app.route("/")
def home():

    # Dataset-la irundhu random question
    question = df.sample(n=1).iloc[0]

    return render_template(
        "index.html",
        role=question["role"],
        question=question["question"]
    )


# Analyze Answer
@app.route("/analyze", methods=["POST"])
def analyze():

    role = request.form["role"]
    question = request.form["question"]
    answer = request.form["answer"]

    result = analyze_answer(
        question,
        answer,
        role
    )

    print(result)

    score = result.get("score", 0)
    feedback = result.get("feedback", "No feedback")

    score_manager.add_score(score)

    save_report(
        question,
        role,
        answer,
        feedback
    )

    return render_template(
        "result.html",
        role=role,
        question=question,
        answer=answer,
        feedback=feedback,
        score=score,
        average=score_manager.average_score(),
        percentage=score_manager.percentage(),
        result_status=score_manager.result()
    )


if __name__ == "__main__":
    app.run(debug=True)