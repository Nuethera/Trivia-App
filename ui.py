from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_text = Label(text=f"Score: 0", font=("Ariel", 15, "normal"), fg="white", bg=THEME_COLOR)
        self.score_text.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=400, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            200,
            width=280,
            text="QUESTION",
            fill=THEME_COLOR,
            font=("Ariel", 20, "italic")
        )
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        false_img = PhotoImage(file="images/false.png")
        true_img = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_img, highlightthickness=0, bd=0, command=self.true_input)
        self.false_button = Button(image=false_img, highlightthickness=0, bd=0, command=self.false_input)
        self.false_button.grid(column=0, row=2)
        self.true_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_text.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text,
                                   text=f"You've reached the end of the quiz.\nScore:{self.quiz.score}/10")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_input(self):
        self.show_answer(self.quiz.check_answer("True"))

    def false_input(self):
        self.show_answer(self.quiz.check_answer("False"))

    def show_answer(self, status):
        if status:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
