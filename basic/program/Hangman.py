#구조도 파악
#Start - Generate a random word - Generate as many blanks as letters in word - Ask the user to guess a letter
#Is the guessed letter in the word?
#Replace the blank with the letter / Lose a life(Draw Figure)
#Are all the blanks filled?
#Have they run out of lives?
#Game Over

#행맨의 목숨 리스트 형성
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']





#문제 리스트 생성
word_list = ["shark", "dolphine", "snake", "tiger", "lion", "dog"]
#무작위 문제 선정
import random
question = random.choice(word_list)
#문제에 맞는 글자수 제시
question_len = len(question)
display = []
#for letter in question:
for i in range(question_len):
    display += "_"
print(display)

#게임이 끝의 여부로 판단하여 반복
#게임이 끝나지 않았을 경우
end_of_game = False
#목숨개수
#오류)))))목숨개수가 아래 반복문 안에 있으면 초기화가 되므로 오류발생
stages_len = len(stages)

while end_of_game == False:
    #사용자가 글자 입력
    guess = input("Write down the letter that you guess.\n").upper()
    #철자 분리된 것과 입력된 글자가 있는지 없는지 여부
    #위치 알아내기 - 위치에 있는 글자가 곧 정답의 철자들
    for position in range(question_len):
        question_letter = question[position]
        #글자를 맞출 때
        if question_letter == guess:
            display[position] = guess
        #오류))))) else로 구조를 작성하면 각 철자를 계산할 때마다 목숨감소하므로 별도로 구성

        # #글자를 틀릴 때
        # else:
        #     # 목숨개수
        #     stages_len = len(stages)
        #     #목숨 한개씩 감소
        #     stages_len -= 1
        #     #목숨얼마나 남았는지 출력 : 목숨개수 = 목숨 idx
        #     print(stages[stages_len-1])
    print(f"{' '.join(display)}")


    #철자와 입력된 글자가 일치하지 않을 경우
    if guess not in question:
        if stages_len > 0:
            #목숨 한개씩 감소
            stages_len -= 1
            #목숨 얼마나 남았는지 출력 : 목숨개수 = 목숨 idx
            print(stages[stages_len-1])
        else:
            end_of_game = True
            print("You lose")

    #display에 _가 없다면 끝난 게임
    if "_" not in display:
        end_of_game = True
        print("You win")