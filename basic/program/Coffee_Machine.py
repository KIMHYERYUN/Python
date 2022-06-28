#커피종류 : 각 제조법
#재료 충분한지  - report
#커피 종류 중 원하는 것
#동전 넣기
#많을경우 잔돈 적을경우 종료, 그대로 돈 돌려줌
#커피 출력 및 재료소진
#자판기 반복

from Coffee_Machine_Source import resources, profit, MENU


#TODO 2 : 재료 충분한지 함수 정의
# 재료가 충분한지 확인
def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True

#TODO 3 : 돈이 충분한지 함수 정의
def process_coins():
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total

def is_transaction_successful(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost)
        print(f"Here is ${change} in change")
        #자판기 수익료 계산
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded")
        return False

#TODO 4 : 커피 제조
def coffee_make(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -=order_ingredients[item]
    print(f"Here is your {drink_name}. Enjoy it")

#자판기 사용여부
is_on = True

while is_on:
    #TODO 1 : 커피 선택
    select = input("What would you like? (espresso/latte/capppuccino): ").lower()
    if select == "off":
        is_on = False
    elif select == "report":
        print(f"Water: {resources['water']}ml")
        print(f"milk: {resources['milk']}ml")
        print(f"coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        #선택된 메뉴
        drink = MENU[select]
        #재료 충분한지 여부
        if is_resource_sufficient(drink["ingredients"]):
            #동전 충분한지 여부
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                #커피 제조
                coffee_make(select, drink["ingredients"])
