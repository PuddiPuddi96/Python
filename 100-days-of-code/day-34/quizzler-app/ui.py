from tkinter import Button, Canvas, Label, PhotoImage,  Tk
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
QUESTION_FONT = ("Arial", 16, "italic")


class QuizInterface():
    
    def __init__(self, quiz_brain: QuizBrain):
        self.window = Tk()
        self.quiz = quiz_brain
        self.question_text = ""
        self.__set_up_interface()
        self.__set_up_question_area()
        self.window.mainloop()


    def __set_up_interface(self):
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)
        self.__set_up_score_label()
        self.__set_up_button()
    

    def __set_up_score_label(self):
        self.label_score = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.label_score.grid(row=0, column=1)


    def __set_up_question_area(self):
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.canvas_question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text=self.question_text,
            fill=THEME_COLOR,
            font=QUESTION_FONT)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        self.question_text = self.__get_next_question()
    

    def __set_up_button(self):
        self.true_image = PhotoImage(file="./images/true.png")
        self.false_image = PhotoImage(file="./images/false.png")

        # Why self.? https://www.youtube.com/watch?v=4MKO0knAAKo

        self.button_true = Button(image=self.true_image, command=lambda:self.__check_answer("true"),  highlightthickness=0)
        self.button_false = Button(image=self.false_image, command=lambda:self.__check_answer("false"), highlightthickness=0)

        self.button_true.grid(row=2, column=0)
        self.button_false.grid(row=2, column=1)
    

    def __get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.label_score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.canvas_question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.canvas_question_text, text="You've reached the end of the quiz.")
            self.button_true.config(state="disabled")
            self.button_false.config(state="disabled")
    

    def __check_answer(self, answer:str):
        self.__give_feedback(self.quiz.check_answer(answer))
    

    def __give_feedback(self, is_right:bool):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.__get_next_question)
