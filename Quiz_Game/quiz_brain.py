class QuizBrain:

    def __init__(self, questions_list):
        self.questions_list = questions_list
        self.question_number = 0
        self.score = 0

    # TODO: 1 Asking the questions
    def next_question(self):
        current_question = self.questions_list[self.question_number]
        user_answer = input(f"Q.{self.question_number + 1}: {current_question.text} "
                            f"(True/False): ")
        self.question_number += 1
        self.check_answer(user_answer, current_question.answer)
        return self.score

    # TODO: checking if we're at the end of the quiz.
    def has_questions(self):
        return self.question_number < len(self.questions_list)

    # TODO: 2 checking if the answer was correct
    def check_answer(self, user_answer, question_answer):
        if user_answer.upper() == question_answer.upper():
            self.score += 1
            print(f"You got it right!")
        else:
            print(f"That's wrong.")
        print(f"The correct answer was: {question_answer}")
        print(f"Your current score is:  {self.score}/{self.question_number}")
        print("\n")
