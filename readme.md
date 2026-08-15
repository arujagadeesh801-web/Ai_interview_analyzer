🤖 AI Interview Coach

An AI-powered web application designed to help users practice interviews, analyze their answers, and improve their interview performance through personalized AI feedback.

📌 Project Overview

AI Interview Coach simulates an interview environment where users can answer interview questions using text or voice input.

The application uses AI to analyze the candidate's answer and provides a score, strengths, weaknesses, feedback, and an improved answer.

🚀 Features

- 🎯 Random Interview Question Generator
- 🎤 Voice Input / Speech-to-Text
- 🤖 AI-powered Answer Analysis
- 📊 Interview Performance Scoring
- 💪 Strengths Identification
- ⚠️ Weakness Analysis
- 💡 Personalized Feedback
- ✨ Improved Answer Suggestions
- 📄 Resume Upload
- 📥 PDF Interview Report
- 📚 Interview History
- 📈 Average Score Visualization

🛠️ Technologies Used

Backend

- Python
- Flask

Frontend

- HTML
- CSS
- JavaScript

AI Integration

- OpenRouter API
- Large Language Model for interview answer analysis

Data & Utilities

- CSV
- Pandas
- ReportLab

Development & Deployment

- Git
- GitHub
- Vercel

🧠 How It Works

User
  ↓
Interview Question
  ↓
Text / Voice Answer
  ↓
AI Analysis
  ↓
Score
  ↓
Strengths & Weaknesses
  ↓
Personalized Feedback
  ↓
Improved Answer
  ↓
Interview Report

🤖 AI Analysis

The AI analyzes the candidate's response and generates:

- Score
- Strengths
- Weaknesses
- Feedback
- Improved Answer

This helps users identify areas for improvement and practice better responses for future interviews.

🎤 Voice Input

The application supports voice-based answer input using Speech-to-Text, allowing users to answer interview questions naturally.

📄 Resume Upload

Users can upload their resume as part of the interview preparation process.

📊 Interview History

The application stores interview results so users can review their previous performance and track their progress.

An Average Score Graph provides a visual representation of interview performance.

📥 PDF Report

After completing an interview, users can generate a PDF report containing the interview results and AI-generated feedback.

📂 Project Structure

AI-Interview-Coach/
│
├── app.py
├── ai_analyzer.py
├── questions.py
├── report_generator.py
├── score_manager.py
│
├── dataset/
│   └── interview_questions.csv
│
├── templates/
│   └── HTML files
│
├── static/
│   ├── CSS
│   └── JavaScript
│
├── requirements.txt
└── README.md

⚙️ Installation

Clone the repository:

git clone YOUR_GITHUB_REPOSITORY_URL

Navigate to the project directory:

cd AI-Interview-Coach

Install the required Python packages:

pip install -r requirements.txt

🔐 Environment Variables

The application requires an OpenRouter API key.

Create an environment variable:

OPENROUTER_API_KEY=your_api_key_here

⚠️ Never upload your actual API key to GitHub.

▶️ Run the Application

python app.py

Open the Flask application URL displayed in the terminal.

🌐 Deployment

The application was deployed using Vercel and the source code is maintained using GitHub.

🎯 Future Improvements

- 🎙️ Advanced voice analysis
- 🗣️ Communication and fluency analysis
- 🎯 Personalized interview difficulty
- 📊 More detailed performance analytics
- 🧑‍💼 Multiple interview categories
- 🤖 Support for multiple AI models
- 💬 Real-time interview conversation

👨‍💻 Author

Jagadeesh

GitHub: "arujagadeesh801-web"

---

⭐ If you find this project useful, consider giving it a star!
