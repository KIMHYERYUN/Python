#attributes
#question_number = 0
#questions_list
#리스트에서 질문 가져오기

#methods
#next_question()

class QuizBrain():
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0
        #q_list 값을 question_list에 들여보냄

    # 퀴즈 지속적으로 진행 여부 - 질문번호가 질문지 숫자보다 작으면 True
    def still_question(self):
        '''continue the quiz'''
        if self.question_number == len(self.question_list):
            print("You've completed the quiz")
            print(f"Your final score was: {self.score}/{self.question_number}")
            return False
        elif self.question_number < len(self.question_list):
            return True
        else:
            return False
        # if self.question_number < len(self.question_list): 만을 작성해도 위에 값과 동일


    #질문 추출하기
    def next_question(self):
        '''Give a question and quesiton number increased'''
        #question 리스트에서 질문 추출
        current_question = self.question_list[self.question_number]
        #질문번호 1부터 시작 - 한개씩 증가
        self.question_number += 1
        #질문 출력하고 답변받기
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        #받은 답변과 맞춰보기 - 채점
        self.check_answer(user_answer, current_question.answer)


    #답변확인하기 - score이라는 변수 추가
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")



