#입력된 값을 변수에 대입
text = input("Write down something that you want to count ")
#해당 변수의 길이측정하는 함수 len 사용
print(len(text))
#한줄로 코딩도 가능
print(len(input("Write down something that you want to count")))


#len("string") : 변수의 길이를 측정하는 함수

num_char = len(input("What's your name?"))
print("Your name has " + str(num_char) + " characters.")
#print("Your name has " + num_char + " characters.")
#TypeError: unsupported operand type(s) for +: 'int' and 'str'