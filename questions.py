import random

questions = {

    "HR": [
        "Tell me about yourself.",
        "What are your strengths and weaknesses?",
        "Why should we hire you?"
    ],

    "Technical": [
        "Explain deadlock in Operating System.",
        "What is Object Oriented Programming?",
        "Explain database normalization."
    ],

    "Aptitude": [
        "A train travels 60 km in 1 hour. Find the speed.",
        "What is 25% of 200?",
        "If x + 5 = 10, find x."
    ]
}


def get_question(category):
    return random.choice(questions[category])