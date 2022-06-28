#for 반복문 : 리스트 안에 있는 요소들을 반복하여

# for item in list_of_items:
#     #Do something to each item

# for number in range(a, b):
#     print(number)


#for 요소 in 리스트 : [요소1, 요소2...]
#for 반복문이 적용되는 구간 확인
fruits = ["Apple", "Banana", "Watermelon"]
for fruit in fruits:
    print(fruit)
    print(fruit + " Pie")
# Apple
# Apple Pie
# Banana
# Banana Pie
# Watermelon
# Watermelon Pie

for fruit in fruits:
    print(fruit)
print(fruit + " Pie")
# Apple
# Banana
# Watermelon
# Watermelon Pie


#1~100까지의 모든 합
total = 0
for number in range(1, 101):
    total += number
print(total)

#String 타입에서도 하나씩 철자 추출 가능
for letter in "Banana":
    print(letter)
# B
# a
# n
# a
# n
# a
