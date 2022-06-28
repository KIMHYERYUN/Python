#def function() :
#   do something
#   return result
#함수 적용 시 result 도출

#len : 입출력 둘다 동시에 갖는 함수

#입력된 이름 - 첫글자 대문자로 변환 함수 정의
def format_name1(first_person_name, second_person_name):
    print(first_person_name.title())
    print(second_person_name.title())

def format_name2(first_person_name, second_person_name):
    formated_first_person_name = first_person_name.title()
    formated_second_person_name = second_person_name.title()
    print(f"{formated_first_person_name}, {formated_second_person_name}")

def format_name3(first_person_name, second_person_name):
    formated_first_person_name = first_person_name.title()
    formated_second_person_name = second_person_name.title()
    return f"{formated_first_person_name}, {formated_second_person_name}"

format_name1("KIM", "hYerYUN")
#Kim
#Hyeryun
format_name2("KIM", "hYerYUN")
#Kim, Hyeryun
print(format_name3("KIM", "hYerYUN"))
#Kim, Hyeryun
format_name3("KIM", "hYerYUN")
#미출력
print(format_name3(input("What is your last name?"), input("What is your first name?")))




#return 값이 없는 경우

def format_name4(first_person_name, second_person_name):
    #입력값이 없는 경우 리턴 값은 없음
    if first_person_name == "" or second_person_name == "":
        return
        #return print("You didn't enter the name")
    formated_first_person_name = first_person_name.title()
    formated_second_person_name = second_person_name.title()
    return f"{formated_first_person_name}, {formated_second_person_name}"

#입력값이 없는 경우 -> None