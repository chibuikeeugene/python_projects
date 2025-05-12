import tkinter as tk
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizInterface:

    """quiz user interface"""

    def __init__(self, quiz_brain:QuizBrain):
        self.quiz = quiz_brain
        self.window = tk.Tk() # create a new tkinter window application
        self.window.title('Quizzler')
        self.window.minsize(300,300)

        self.window.configure(background=THEME_COLOR,
                              padx=20,
                              pady=20
                              )


        # create the score label
        self.score_label = tk.Label(text= f'Score: {0}',
                               padx=20,
                               pady=20,
                               background=THEME_COLOR,
                               justify='right')
        self.score_label.grid(row=0, column=1) # getting the score label to show up on screen

        # create the canvas
        self.canvas = tk.Canvas(background='white', height=250, width=300)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=40)

        question_text = self.get_next_qeustion()
        self.canvas_text = self.canvas.create_text(
            150,
            125,
            width=200,
            text=question_text,
            fill=THEME_COLOR,
            font=('Arial', 20, 'italic'))

        # create the button
        true = tk.PhotoImage(file='quizzler-app-start/images/true.png')
        self.correct_button = tk.Button(image=true, command=self.select_true)
        self.correct_button.grid(row=2, column=0)

        false =  tk.PhotoImage(file='quizzler-app-start/images/false.png')
        self.wrong_button = tk.Button(image=false, command=self.select_false)
        self.wrong_button.grid(row=2, column=1)

        self.window.mainloop()
    
    def get_next_qeustion(self) -> str:
        """return the next quiz question """
        return self.quiz.next_question()
    
    def get_correct_answer(self):
        """check if user's answer matches the correct answer"""
        self.quiz.check_answer()

    def select_true(self) -> bool:
        """return user true selection"""
        return True
    
    def select_false(self) -> bool:
        """return user false selection"""
        return False

