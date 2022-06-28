#이것보다 클까 작을까를 맞추는 게임
#스코어 : 맞춘 갯수
#재실행

#로고 출력
from replit import clear

from Higher_Lower_Game_Art import logo, vs

print(logo)

#랜덤 문제 출제
import random

#문제파일 가져오기
from Higher_Lower_Game_Data import data

#문제파일 한개 가져오기
problem_a = random.choice(data)

#게임 지속여부
is_game_over = False
#게임 스코어
score = 0

while not is_game_over:
    #두번째 문제 제시
    problem_b = random.choice(data)

    #첫번째 두번째 문제가 같은 경우 다시 제시
    if problem_a == problem_b:
        problem_b = random.choice(data)

    #문제 출력
    def format_problem(problem):
        """Format the account data into printable format."""
        #for key in problem.keys():
        problem_name = problem["name"]
        problem_descr = problem["description"]
        problem_country = problem["country"]
        return f"{problem_name}, a {problem_descr}, from {problem_country}"
        ###오류 : print로 출력할 경우 아래 문제 프린트에서 재사용 불가하므로 return 사용

    #A문제 프린트
    print(f"Compare A : {format_problem(problem_a)}.")
    #vs로고 프린트
    print(vs)
    #B문제 프린트
    print(f"Compare B : {format_problem(problem_b)}.")

    #Ask user for a guess
    guess = input("Who has more followers? Type 'A' or 'B': ")

    #답 추출
    def compare_number(problem_a, problem_b):
        if problem_a["follower_count"] > problem_b["follower_count"]:
            return 'A'
        else:
            #다음 출제를 위해 문제 바꾸기
            problem_a = problem_b
            return 'B'

    #답이 맞으면 다른 문제 출제, 스코어 +1
    if guess == compare_number(problem_a, problem_b):
        #스코어 1 증가
        score += 1
        print(f"You're right! Current score: {score}")
    else:
        is_game_over = True
        print(f"You're lose! Current score: {score}")
        again_play = input("Do you want to play again? Y or N ").lower()
        if again_play == 'y':
            clear()
            is_game_over = False
        else:
            print("Bye bye")

#다른 방법 : 비교와 답 확인을 한번해 할 수 있는 함수 정의
def check_answer(guess, a_followers, b_followers):
  """Checks followers against user's guess
  and returns True if they got it right.
  Or False if they got it wrong."""
  if a_followers > b_followers:
    return guess == "a"
  else:
    return guess == "b"

