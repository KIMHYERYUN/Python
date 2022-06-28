#알아보고 싶은 윤년의 입력값
year = int(input("Which year do you want to check?"))
#윤년의 정의 : 4의 배수이나, 100의 배수 제외, 400의 배수 포함

if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is leap year")
else:
    print(f"{year} is not leap year")

#다른방법
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year")
        else:
            print("Not Leap year")
    else:
        print("Leap year")
else:
    print("Not Leap year")
