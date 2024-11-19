

class QuizBrain:
    def __init__(self, q_list) -> None:
        self.question_no = 0
        self.question_list = q_list
        self.score = 0
    

    # TODO: 1. asking the question
    def next_question(self): # retrieve the next question from the question list
         self.current_question = self.question_list[self.question_no]
         self.question_no += 1
         self.user_response = input(f'Q{self.question_no}: {self.current_question.text} (True/False)?:')
         self.is_user_input_correct(self.user_response, self.current_question.answer)


    # TODO: 2. checking if the answer is correct
    def is_user_input_correct(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score +=1
            print('you got it right.')
        else:
            print('That\'s wrong.')
        print(f'The correct answer was: {correct_answer}')
        print(f'Your current score is: {self.score}/{self.question_no}')
        print('\n')


    # TODO: 3. checking if we are at the end of the quiz
    def still_has_questions(self) -> bool:
        return self.question_no < len(self.question_list)