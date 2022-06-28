#
print("Welcome to the Hyeryun tip calculator.")
bill = input("What was the total bill?\n$")
percentage = input("What percentage tip would you like to give? 10, 12, or 15?\n")
people = input("How many people to split the bill?\n")

tip = float(bill) * (int(percentage) / 100)
total = float(bill) + tip
print(type(total))
each_pay = round(total / int(people), 3)
print(type(each_pay))

#방법 1
print(f"Each person should pay: ${each_pay}")
#방법 2
print("Each person should pay: " + "$" + str(each_pay))



#다른답안
#애초에 type 변환 후 연산작업
bill = float(input("What was the total bill?\n$"))
percentage = int(input("What percentage tip would you like to give? 10, 12, or 15?\n"))
people = int(input("How many people to split the bill?\n"))
total = bill * (percentage / 100) + bill
each_pay = total / people
#특정형식(소수점 이하 둘째자리까지) 형태로 적용
final_amount = "{:.2f}".format(each_pay)
print(f"Each person should pay: ${final_amount}")
