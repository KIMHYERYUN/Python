#1~100까지 짝수의 모든 합
total_1 = 0
for number in range(0, 101, 2):
    total_1 += number
print(total_1)

#다른 방법
total_2 = 0
for number in range(1, 101):
    if number % 2 == 0:
        total_2 += number
print(total_2)