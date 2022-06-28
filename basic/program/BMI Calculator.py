#bmi 계산 시 필요한 요소 정의
height = float(input("Enter you height in m: "))
weight = float(input("Enter you weight in kg: "))
#bmi 계산법
bmi = height / weight ** 2
#bmi 영역에 해당하는 등급
if(bmi <= 18.5):
    print(f"Your bmi is {bmi}, you are underweight.")
elif(bmi < 25):
    print(f"Your bmi is {bmi}, you are a normal weight.")
elif(bmi < 30):
    print(f"Your bmi is {bmi}, you are a overweight.")
elif(bmi < 35):
    print(f"Your bmi is {bmi}, you are a obese.")
else:
    print(f"Your bmi is {bmi}, you are clinically obese.")