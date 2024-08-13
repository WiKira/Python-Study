from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for new_q in question_data:
    question_bank.append(Question(new_q["question"], new_q["correct_answer"]))

quiz = QuizBrain(question_bank)

final_score = 0

while quiz.has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
