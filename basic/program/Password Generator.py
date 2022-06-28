#비밀번호 생성기

#사용할 문자 정의
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


#각 인덱스 구하기 - 범위안에서 정수 난수 생성 - 추출 : 이 과정을 횟수만큼
#비밀번호 만들기 - 단순 더하는 과정
password_simple = ""
for n in range(0, nr_letters):
    random_letters = random.choice(letters)
    password_simple += random_letters
for n in range(0, nr_symbols):
    random_symbols = random.choice(symbols)
    password_simple += random_symbols
for n in range(0, nr_numbers):
    random_numbers = random.choice(numbers)
    password_simple += random_numbers
print(password_simple)
print(f"Your simple password is: {password_simple}")

#비밀번호 만들기 - 리스트로 만들어서 랜덤하게 만드는 과정
password_diff_list = []
for n in range(0, nr_letters):
    random_letters = random.choice(letters)
    password_diff_list.append(random_letters)
for n in range(0, nr_symbols):
    random_symbols = random.choice(symbols)
    password_diff_list.append(random_symbols)
for n in range(0, nr_numbers):
    random_numbers = random.choice(numbers)
    password_diff_list.append(random_numbers)
#각 범위 내에서 생성된 비밀번호 리스트 출력
print(password_diff_list)

#비밀번호 리스트 내에서 무작위 선출 - (0, 길이-1)만큼
password_diff = ""
for n in range(0, len(password_diff_list)):
   password_diff += random.choice(password_diff_list)

#random.shuffle(password_diff_list)
#for char in password_diff_list:
#    password_diff += char

print(password_diff)
print(f"Your difficult password is: {password_diff}")






