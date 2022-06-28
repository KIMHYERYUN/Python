#가위바위보 게임 만들기
#가위바위보 정의
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#위 가위바위보 이미지 리스트화
game_images = [rock, paper, scissors]


#사용자가 가위바위보 낼 패 입력
#users가 낸 것 - str으로 정수로 변환
users = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors\n"))
#컴퓨터가 가위바위보 낼 패 정수 난수정하기 - random 모듈
import random
#0, 1, 2 중 정수 난수 구하기 위해 randint(0, 3) : 0이상 2이하의 정수
computers = random.randint(0, 2)
#users, computers가 낸 것 출력
print(f"You chose {users}")
print(game_images[users])
print(f"Computers chose {computers}")
print(game_images[computers])

#각 상황 예측하여 모델생성
'''
0-0 : same
0-1 : lose
0-2 : win

1-0 : win
1-1 : same
1-2 : lose

2-0 : lose
2-1 : win
2-2 : same
'''
#users가 낼 수 있는 것, computers가 낼 수 있는 것을 리스트화 : 중첩 리스트 games
row_rock = ["same", "lose", "win"]
row_paper = ["win", "same", "lose"]
row_scissors = ["lose", "win", "same"]
games = [row_rock, row_paper, row_scissors]

#users가 낸 것, computers가 낸 것 : 결과 추출
result = games[users][computers]

print("you " + result)





print("두번째 게임 : 다른방법")
#그러나 버그 존재 : 0, 1, 2 이외의 숫자 입력시 경고문, 조금 더 가위바위보 결과를 묶을 수 있도록 조건문 사용
users = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors\n"))

#(추가)0, 1, 2 일 경우와 이외의 경우 - 조건문
if users >= 3 or users < 0:
    print("You typed an invalid numer, you lose")
else:
    #컴퓨터가 가위바위보 낼 패 정수 난수정하기 - random 모듈
    import random
    #0, 1, 2 중 정수 난수 구하기 위해 randint(0, 2) : 0이상 2이하의 정수
    computers = random.randint(0, 2)
    #users, computers가 낸 것 출력
    print(f"You chose {users}")
    print(game_images[users])
    print(f"Computers chose {computers}")
    print(game_images[computers])

    #각 상황 예측하여 모델생성
    '''
    0-0 : same
    0-1 : lose
    0-2 : win
    
    1-0 : win
    1-1 : same
    1-2 : lose
    
    2-0 : lose
    2-1 : win
    2-2 : same
    '''
    #숫자 형태로 크고 작고 같은 부분을 가지고 조건문 생성
    #세분화하여 나누기
    if users == computers:
        print("It's draw")
    elif users == 0 and computers == 2:
        print("You're Win")
    elif users < computers:
        print("You're lose")
    elif users == 2 and computers == 0:
        print("You're lose")
    elif users > computers:
        print("You're win")

    # #위 내용 간단히 합치기
    # if users == computers:
    #     print("It's draw")
    # elif (users == 0 and computers == 2) or users > computers:
    #     print("You're Win")
    # elif users < computers or (users == 2 and computers == 0):
    #     print("You're lose")