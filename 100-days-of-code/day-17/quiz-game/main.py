from question_model import Question
from data import question_data
from data_2 import question_data_2
from quiz_brain import QuizBrain

question_bank = []
for element in question_data_2:
    question_bank.append(
        Question(
            element["question"],
            element["correct_answer"]
        )
    )

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your finale score was {quiz.score}/{quiz.question_number} ")
