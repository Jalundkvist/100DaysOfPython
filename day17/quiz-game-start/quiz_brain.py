class QuizzBrain:
    """QuizzBrain game class"""

    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def next_question(self):
        """Updates the current question number"""
        question = self.question_list[self.question_number]
        self.question_number += 1

        while True:
            print(f"Question {self.question_number}: {question.text} (True or False)")
            answer = input("Input: ").lower()

            if answer == 'true':
                answer = "True"
                break
            elif answer == 'false':
                answer = "False"
                break
            print('Invalid input\n\n')
        self.check_answer(answer, question.answer)

    def check_answer(self, answer, question):
        if answer == question:
            self.score += 1
            print('Correct!')
        else:
            print("That's incorrect.")
        print(f'The correct answer was {question}')
        print(f'Your score: {self.score}/{self.question_number}')

    def still_has_questions(self):
        return self.question_number < len(self.question_list)
