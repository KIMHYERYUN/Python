#FizzBuzz 게임 만들기

#3으로 나누는 경우 : Fizz
#5로 나누는 경우 : Buzz
#15로 나누는 경우 : FizzBuzz

n = int(input("Enter the range number 'n' : (1, n) \n"))

for number in range(1, n):
    if number % 15 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)