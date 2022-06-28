#로고 출력
from Calculator_Art import logo
print(logo)

#return(반환)과 출력의 차이 : 별도의 변수 삽입없이 값을 이용할 수 있다
def add(num1, num2):
    return num1 + num2
def subtract(num1, num2):
    return num1 - num2
def multiply(num1, num2):
    return num1 * num2
def divide(num1, num2):
    return num1 / num2

#연산자 dictionary 만들기 - 추출
operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}
def calculator():
    # 첫번째 숫자 입력
    num1 = float(input("What's the first number?: "))
    # 연산자의 종류 나타내기
    for symbol in operations:
        print(symbol)

    should_continue = True
    while should_continue:
        # 연산자 입력받기
        operation_symbol = input("Pick an operation from the line above: ")
        # 다음 숫자 입력
        num2 = float(input("What's the second number?: "))
        # 결과값
        result = operations[operation_symbol](num1, num2)
        # 출력
        print(f"{num1} {operation_symbol} {num2} is {result}")

        #추가 계산 여부
        should_continue = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ").lower()
        if should_continue == "y":
            num1 = result
        elif should_continue == "n":
            should_continue = False
            #새로운 계산기 실행
            calculator()
        else:
            should_continue = False
            print("Your answer is wrong. Calculator is exited.")


calculator()