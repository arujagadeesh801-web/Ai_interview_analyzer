import os
import re
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")


def analyze_answer(question, answer, role="Software Engineer"):

    url = "https://openrouter.ai/api/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    prompt = f"""
You are an AI Interview Coach.

Analyze the candidate answer for this interview.

Role: {role}

Question:
{question}

Candidate Answer:
{answer}

Give a short evaluation.

Return only:

Score: (0-10)

Strengths:
- Maximum 2 points

Weaknesses:
- Maximum 2 points

Feedback:
- Only 2 or 3 sentences

Improved Answer:
- Give a short correct answer example

Keep everything concise. Avoid long explanations.
"""

    data = {
        "model": "openai/gpt-4o-mini",
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ],
        "temperature": 0.5,
        "max_tokens": 400
    }


    response = requests.post(
        url,
        headers=headers,
        json=data
    )


    result = response.json()


    try:

        feedback = result["choices"][0]["message"]["content"]


        score_match = re.search(
            r"Score:\s*(\d+)",
            feedback
        )


        score = int(score_match.group(1)) if score_match else 0


        return {
            "score": score,
            "feedback": feedback
        }


    except Exception as e:

        return {
            "score": 0,
            "feedback": f"AI analysis failed: {str(e)}"
        }