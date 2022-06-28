#계산 시 필요한 변수 저어의
print("Welcome to Hyeryun Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L")
add_pepperoni = input("Do you want pepperoni? Y or N")
extra_cheese = input("Do you want extra cheese? Y or N")
#bill의 상태를 보여줌(생략 가능)
bill = 0
#각 조건별 설정
if size == "S":
    bill = 15
    if add_pepperoni == "Y":
        bill += 2
elif size == "M":
    bill = 20
elif size == "L":
    bill = 25
    if add_pepperoni == "Y":
        bill += 3
if extra_cheese == "Y":
    bill += 1
else:
    print("Your answer is wrong size")

print(f"Your final bill is: {bill}")



#다른 방법
print("Welcome to Hyeryun Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L")
add_pepperoni = input("Do you want pepperoni? Y or N")
extra_cheese = input("Do you want extra cheese? Y or N")
if size == "S":
    bill = 15
elif size == "M":
    bill = 20
elif size == "L":
    bill = 25

if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1
else:
    print("Your answer is wrong size")

print(f"Your final bill is: {bill}")