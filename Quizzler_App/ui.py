import time
from quiz_brain import QuizBrain
from tkinter import *

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(background=THEME_COLOR, pady=20, padx=20)

        self.score_text = Label(text="Score: 0", background=THEME_COLOR, foreground="white")
        self.score_text.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250)
        self.question_text = self.canvas.create_text(150, 125, text="Question goes over here.",
                                                     width=280,
                                                     font=("Arial", 16, "italic"),
                                                     justify="center")
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        true_png = PhotoImage(file="images/true.png")
        false_png = PhotoImage(file="images/false.png")
        self.true_button = Button(image=true_png, highlightthickness=0, command=self.true_button_pressed)
        self.true_button.grid(column=0, row=2)
        self.false_button = Button(image=false_png, highlightthickness=0, command=self.false_button_pressed)
        self.false_button.grid(column=1, row=2)
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(background="white")
        if self.quiz.still_has_questions():
            question = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=question)
        else:
            self.canvas.itemconfig(self.question_text, text=f"You've reached the end of the quiz."
                                                            f"\nScore: {self.quiz.score}/10", justify="center")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_button_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_button_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, param: bool):
        if param:
            self.canvas.config(bg="green")
            self.score_text.config(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)
