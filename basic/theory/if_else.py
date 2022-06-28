#if condition1:
#   do A
#elif condition2:
#   do B
#else:
#   do this

#순서 : 1-2-3-4-5-6


#if condition1:
#   do A
#if condition2:
#   do B
#if condition3:
#   do C

#if-elif-else vs if-if-if
#결과값이 다름 : A,B,C 중 하나 vs A,B,C 다중 가능


#키가 120이상이면 탑승가능, 그렇지않으면 불가
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
parent_with = input("Are you with parent? True or False")
if height >= 120:
    if(parent_with == True):
        print("You can ride the rollercoaster!")
    else:
        print("Sorry, you can't ride the rollercoaster without parent.")
elif height < 120:
    print("Sorry, you have to grow taller before you can ride.")
else:
    print("You answer is wrong.")

# 키가 120이상이면 탑승가능, 그렇지않으면 불가 + 추가금액 + 조건문 추가(사진촬영여부)
if height >=120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age?"))
    if age < 12:
        bill = 5
        print("Child tickets are $5")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7")
    elif age >= 45 and age <= 55:
        print("Everything is goin to be ok. Have a free ride on us!")
    else:
        bill = 12
        print("Adult tickets are $12")
    wants_photo = input("Do you want a photo taken? Y or N")
    if wants_photo == y:
        bill += 3
        print(f"Your final bill is {bill}")
    else:
        print(f"Your final bill is {bill}")
else:
    print("Sorry, you have to grow taller before you can ride.")