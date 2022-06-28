#FPSBA : First-price sealed-bid auction
#비밀경매프로그램 : 로고 - 이름 - 입찰가 - 추가 입찰인 존재여부 - 이름 - 입찰가 ----- 마지막 입찰가 - 가장높은 입찰가 입력한 사람 출력

from FPSBA_art import logo
print(logo)


#auction dictionary에서 가장 큰 금액 선정
def find_highest_bidder(auction):
    highest_bid = 0
    winner =""
    for bidder in auction:
        bid_amount = auction[bidder]
        if highest_bid < bid_amount:
           highest_bid = bid_amount
           winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}.")



#실행여부 설정
bidding_finished = False
#실행한다면
while not bidding_finished:
    name = input("What's your name?\n")
    bid = int(input("What's your bid?: $\n"))
    auction = {}

    #auction dictionary에 추가 - 수집
    def add_auction(name, bid):
        auction[name] = bid

    add_auction(name, bid)

    continue_is = input("Are there any other bidders? Type 'yes or 'no'.\n").lower()
    if continue_is == "no":
        bidding_finished == True
        find_highest_bidder(auction)
    elif continue_is != "yes" and continue_is !="no":
        print("Your answer is wrong")
    else:
        bidding_finished == "False"

