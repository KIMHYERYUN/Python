#윤년이 맞는경우 : true
#윤년이 아닌경우 : false

#윤년의 조건 : 4로 나누어지며 100의 배수가 아니거나 400의 배수인경우
def leap_year_is(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print("Leap year")
            else:
                print("Not leap year")
        else:
            print("Leap year")
    else:
        print("Not leap year")

#윤년의 경우와 아닌경우의 일수
def days_in_month(year, month):
    days_in_month_leap = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days_in_month_not_leap = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if leap_year_is(year) == "Leap year":
        days = days_in_month_leap[month - 1]
        return days
    elif leap_year_is(year) == "Not leap year":
        days = days_in_month_not_leap[month - 1]
        return days
    else:
        return print("Your answer is wrong.")

    print(f"{year}년 {month}월은 {days}일이다.")

###오류 : input 시 string이므로 변환 필요
days_in_month(int(input("Write down year\n")), int(input("Write down month\n")))

