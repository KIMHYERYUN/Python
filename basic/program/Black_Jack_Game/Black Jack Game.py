
#게임규칙
#카드 두장의 합이 21이 최대, 넘으면 lose -
#2~10, KQJ = 10, A = 1 or 11(21이상이면 1)
#첫번째 카드는 들어냄
#두번째 카드는 가림 - 단 자신의 패는 볼수있음
#세번째 카드 선택할지 말지 선택 - 17미만일경우 세번째카드 선택

#로고 삽입
from Black_Jack_Game_Art import logo
#로고 출력
print(logo)

#콘솔을 지울 수 있는 명령어
from replit import clear


def play_game():
    #랜덤카드 부여하는 함수 만들기
    import random

    def deal_card():
        """Return a random card from the deck"""
        # 카드종류
        cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
            # {"1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "K": 10, "Q": 10, "J": 10,"A": 11}
        # 카드 한장 선택
        card = random.choice(cards)
        return card

    #사용자와 컴퓨터의 패
    user_cards = []
    computer_cards = []

    #각 두장씩 카드 부여
    for _ in range(2):
        #new_card = deal_card()
        #user_cards.append()
        #user_cards.extend(new_card) : type 오류( +=와 같은 역할, new_card 자체로 리스트를 추가하는 것이 아닌 하나의 항목을 추가할 경우 append)
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    #append : 한 항목 끝에 추가
    #extend : 리스트를 끝에 추가


    #각 카드의 합계 : 리스트 내의 항목 합계(sum 함수)
    def calculate_score(cards):
        """Take a list of cards and return the score calculated from the cards"""
        #합이 21이고 패가 2장일경우의 합은 0으로 표시
        if sum(cards) == 21 and len(cards) == 2 :
            return 0
        #합이 21보다 크고 패가 11을 가지고 있을 경우 - 11을 지우고 1을 추가
        if sum(cards) > 21 and 11 in cards:
            cards.remove(11)
            cards.append(1)

        return sum(cards)

    #각 카드의 합계구하기
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)


    #게임 진행여부
    is_game_over = False

    #게임이 지속적으로 진행될 경우
    while not is_game_over:
        #각 패를 보여줄 문구 출력
        print(f"     Your cards: {user_cards}, current score: {user_score}")
        print(f"     Computer cards: {computer_cards[0]}")


        #둘 중 한명이 0인경우, 21이 넘는경우
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            #세번째 카드 선택 여부
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ".lower())
            #세번째 카드 추가, 아니면 게임 종료
            if user_should_deal == "y":
                user_cards.appned(deal_card())
            else:
                is_game_over = True

    #컴퓨터의 세번째 카드 가져올지 여부
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        #컴퓨터의 스코어 업데이트
        computer_score = calculate_score(computer_cards)

    #마지막 패 출력
    print(f"     Your final hand: {user_cards}, final score: {user_score}")
    print(f"     Computer final hand: {computer_cards}, final score: {computer_score}")


    #승패를 가리는 함수
    def compare(user_score, computer_score):
        if user_score == computer_score:
            #print("Draw")
            return "Draw"
        elif user_score == 0:
            return "You win, You has a Blackjack"
        elif computer_score == 0:
            return "You lose, Computer has a Blackjack"
        elif user_score > 21:
            return "You lose, Went over"
        elif computer_score > 21:
            return "You win, Computer went over"
        elif user_score > computer_score:
            return "You win, Your score is bigger than computer's"
        else:
            return "You lose, Your score is smaller than computer's"

    #마지막 패 비교하여 승패를 가리기
    print(compare(user_score, computer_score))

play_game()

#새로운 게임 여부
new_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
while new_game == "y":
    #콘솔을 리셋하기
    #from replit import clear 추가
     clear()
     play_game()
