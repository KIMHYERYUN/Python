#Advanced Functions
#Default Arguments : 디폴트 인자 설정하는 방법

#기본적으로 ()안에 도움말을 통해 필수인자 여부 확인
#없는경우 나머지 옵션은 기본값 설정

#기본값은 아무것도 없을시 설정된 값
#추후 변동 가능

'''
import turtle
tim = turtle.Turtle()
tim.write("Hello")


import tkinter
windows = tkinter.Tk()
my_label = tkinter.Label(text="Hello")
my_label.pack()

windows.mainloop()

'''

#Unlimited Positional Arguments
#정의되지 않은 양의 입력을 함수에 전달할 수 있게 하는 방법
#*Arg : 인수 모든 것, 미지정 갯수 입력가능 - tuple 형태로 출력
def add(*args):
    sum_num = 0
    for n in args:
        sum_num += n
    return sum_num
    #오류 : return 부분을 빼먹음

print(add(1, 2, 3, 4, 5))
print(add(1))
print(add())



#Many Keyworded Arguments
#**Kwargs :  가변인수와 인자, 키워드인 이름표를 달고오는 경우 - dict 형태로 출력

def calculate(n, **kwargs):
    print(kwargs)
    print(kwargs["add"])
    #각 key, value 추출 및 접근가능
    for key, value in kwargs.items():
        print(key)
        print(value)



calculate(2, add=3, multiply=5)
#{'add': 3, 'multiply': 5}


'''
class Car:
    def __init__(self, **kw):
        self.make = kw["make"]
        self.model = kw["model"]

my_car = Car(make="kia")
print(my_car.make)
#KeyError: 'model' : Car의 객체 생성시 make, model 두 인자를 가져야 하나 model이 없으므로 오류
'''

class Car_2:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")

my_car_2 = Car_2(make="kia")
print(my_car_2.make)  #kia
#KeyError가 일어나지 않으며 print(my_car_2.model)의 값은 none : get함수는 가져오는 의미로 필수가 아니며 유무 판단