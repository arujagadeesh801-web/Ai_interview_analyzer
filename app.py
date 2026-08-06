from flask import Flask, render_template, request
import pandas as pd
import traceback

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
    question = df.sample(n=1).iloc[0]

    return render_template(
        "index.html",
        role=question["role"],
        question=question["question"]
    )


# Analyze Answer
@app.route("/analyze", methods=["POST"])
def analyze():

    try:
        role = request.form["role"]
        question = request.form["question"]
        answer = request.form["answer"]

        result = analyze_answer(question, answer, role)

        print("AI Result:", result)

        score = result.get("score", 0)
        feedback = result.get("feedback", "No feedback")

        score_manager.add_score(score)

        # Comment this temporarily for testing
        # save_report(question, role, answer, feedback)

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

    except Exception:
        error = traceback.format_exc()
        print(error)
        return f"<pre>{error}</pre>", 500


if __name__ == "__main__":
    app.run(debug=True)
