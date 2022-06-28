#프로그램 순서도
#문제  - True/False
#문제 가져올 수 있는 사이트 : opentdb.com
#맞출경우 - You got it right! / The correct answer was:  / Your current score is : 1/+1
#틀릴경우 - That's wrong. The correct answer was : /  Your current score is : -1/+1
#틀릴경우 - 게임 지속여부, This repl has exited, run again?

#설정값

#문제 불러오기 - 리스트 형식
#from data import question_data
#새로운 문제 불러오기
from data_2 import question_data
from question_model import Question
from quiz_brain import QuizBrain

#question_data를 쉽게 접근하기 위한 question_bank 만들기
#question_bank = [Question(q1, a1), Question(q2, a2),....]
#데이터에서 추출하여 변수로 지정 - 그것을 Question이라는 객체로 전달하여 question_bank로 삽입하여 리스트 형성
question_bank = []
for question in question_data:
    #question_text = question["text"]
    question_text = question["question"]
    #question_answer = question["answer"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

#print(question_bank[0].answer)


quiz = QuizBrain(question_bank)


#지속적으로 quiz 진행여부
while quiz.still_question():
    quiz.next_question()


#main에 직접 속성을 가지고 표현하고 싶을때
#print("You've completed the quiz")
#print(f"Your final score was: {quiz.score}/{quiz.question_number}")

