import os
from datetime import datetime

def save_report(question, role, answer, ai_feedback):

    if not os.path.exists("reports"):
        os.makedirs("reports")

    filename = f"reports/interview_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"

    with open(filename, "w", encoding="utf-8") as file:
        file.write("===== AI Interview Report =====\n\n")
        file.write(f"Date: {datetime.now()}\n\n")
        file.write(f"Role: {role}\n\n")
        file.write(f"Question:\n{question}\n\n")
        file.write(f"Candidate Answer:\n{answer}\n\n")
        file.write("===== AI Evaluation =====\n")
        file.write(ai_feedback)

    return filename