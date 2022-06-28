#입력된 숫자의 각 자리의 숫자를 더한 값 출력
two_digit_number = input("Type a two digit number: ")
#first_digit_number = int(two_digit_number)[0]
#second_digit_number = int(two_digit_number)[1]
#문자열에서만 [] index 적용 가능

first_digit_number = two_digit_number[0]
second_digit_number = two_digit_number[1]

print(int(first_digit_number) + int(second_digit_number))

#추가)변수를 활용한 방법
result = int(first_digit_number) + int(second_digit_number)
print(result)
