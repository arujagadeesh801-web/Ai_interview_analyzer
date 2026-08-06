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
        "Content-Type": "application/json",
        "HTTP-Referer": "https://ai-interview-analyzer.vercel.app",
        "X-Title": "AI Interview Analyzer"
    }

    prompt = f"""
You are an AI Interview Coach.

Role: {role}

Question:
{question}

Candidate Answer:
{answer}

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
"""

    payload = {
        "model": "openrouter/free",
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ],
        "temperature": 0.5,
        "max_tokens": 400
    }

    try:
        response = requests.post(
            url,
            headers=headers,
            json=payload,
            timeout=30
        )

        result = response.json()

        print(result)

        if "choices" not in result:
            return {
                "score": 0,
                "feedback": result.get("error", {}).get("message", str(result))
            }

        feedback = result["choices"][0]["message"]["content"]

        match = re.search(r"Score:\s*(\d+)", feedback)
        score = int(match.group(1)) if match else 0

        return {
            "score": score,
            "feedback": feedback
        }

    except Exception as e:
        return {
            "score": 0,
            "feedback": str(e)
        }
