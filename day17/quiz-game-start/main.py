from question_model import Question
from data import question_data
from quiz_brain import QuizzBrain

question_bank = [Question(question["question"], question["correct_answer"]) for question in question_data]
quiz_game = QuizzBrain(question_bank)


while quiz_game.still_has_questions():
    quiz_game.next_question()
