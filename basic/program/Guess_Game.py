from replit import clear
from Guess_Game_Art import logo

print(logo)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")

def game_start():
    #맞출 숫자 1~100 선택
    import random
    number_correct = random.choice(range(1, 101))

    #난이도 선택
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

    #난이도에 따른 목숨갯수
    if level == "easy":
        live = 10
    else:
        live = 5

    #게임 계속 진행여부 - 목숨이 남았을 경우
    is_game_over = False
    while not is_game_over:
        if live > 0:
            #목숨 갯수 출력 - 숫자 입력받기
            print(f"You have {live} attempts remaining to guess the number.")
            guess = int(input("Make a guess: "))
            #맞출경우, 못맞출경우 목숨 - 1
            if guess == number_correct:
               is_game_over = True
               print("You correct")
            else:
               live -= 1
               # 힌트주기 : 입력한 숫자와 비교하여 크고 작은지 출력
               if guess > number_correct:
                   print("Too high")
               else:
                   print("Too low")
               print("Guess Again")
               is_game_over = False
        else:
            is_game_over = True
            print(f"The number is {number_correct}")
            print("You lose")

game_start()

#새로운 게임 시작 여부묻기
game_again = input("Do you want a new game? Y or N ").lower()
while game_again == "y":
    clear()
    game_start()
