from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

#객체 생성
#객체명 : 소문자와 언더바 대개 이용
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()
#on/off 변수 만들기
is_on = True



while is_on:
    #메뉴 불러오기
    options = menu.get_items()
    #메뉴 선택하기
    choice = input(f"What would you like? ({options} : ")
    #메뉴 선택에 따른 행동
    #off - 자판기 off
    if choice == "off":
        is_on = False
    #report - 현재상태 불러오기 - report 함수 활용
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    #음료 선택 - 입력한 음료가 실제 있는지 여부 확인하는 find_drink 함수 활용
    else:
        drink = menu.find_drink(choice)
        #print(drink)
        #선택한 음료가 실제 재료가 충분한지 여부 확인하는 is_resource_sufficient 함수 활용 - boolean
        #print(coffee_maker.is_resource_sufficient(drink))
        #재료가 충분하다면 돈이 충분한지 여부 확인
        #충분한지 확인하는 money machine의 make_payment 함수 활용
        #두가지 방법
        #is_enough_ingredients = coffee_maker.is_resource_sufficient(drink)
        #is_payment_successful = money_machine.make_payment(drink.cost)
        #if is_enough_ingredients and is_payment_successful:
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink, cost):
            #충분하다면 커피를 만들어 내는 함수 - make coffee
            coffee_maker.make_coffee(drink)
