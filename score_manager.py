class ScoreManager:

    def __init__(self):
        self.total_questions = 0
        self.total_score = 0

    def add_score(self, score):
        self.total_questions += 1
        self.total_score += score

    def average_score(self):
        if self.total_questions == 0:
            return 0
        return round(self.total_score / self.total_questions, 2)

    def percentage(self):
        if self.total_questions == 0:
            return 0
        return round((self.total_score / (self.total_questions * 10)) * 100, 2)

    def result(self):
        if self.percentage() >= 60:
            return "PASS"
        return "NEEDS IMPROVEMENT"