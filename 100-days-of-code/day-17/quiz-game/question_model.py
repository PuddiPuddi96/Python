class Question:


    def __init__(self, question, answer):
        self.question = question
        self.answer = answer


    def __str__(self):
        return f"Question: {self.question}\nAnswer:{self.answer}"