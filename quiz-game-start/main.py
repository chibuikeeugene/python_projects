from data import question_data
from question_model import Question
from quiz_brain import QuizBrain


question_bank = []

for entry in question_data:
    question =  Question(text=entry['text'], answer= entry['answer'])
    question_bank.append(question)

# create a quiz brain object
quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
# call the current question
    quiz.next_question()
        

print('You\'ve completed the quiz.')
print(f'Your final score was: {quiz.score}/{quiz.question_no}')