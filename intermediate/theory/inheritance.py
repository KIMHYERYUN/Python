#class끼리 상속하여 많은 기능 공유
#class 기능을 받는 의미
#Me 클래스가 Mother 클래스를 상속받음
class Mother:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, exhale")

    def walk(self):
        print("arms, legs")

class Me(Mother):
    def __init__(self):
        #상위클래스에서 할 수 있는 것을 전부 초기화 - 기능을 받음
        #상위 클래스의 모든 속성과 메소드를 물려받음
        super().__init__()

    def swim(self):
        print("moving in water")

    #상위클래스의 함수의 기능을 업데이트
    def walk(self):
        #상위클래스의 함수 실행
        super().walk()
        #추가기능
        print("walking the street")

#추가기능 전
kim = Me()
kim.breathe()
kim.swim()
print(kim.num_eyes)
#Inhale, exhale
#moving in water
#2

#추가기능 후
kim = Me()
kim.walk()
#arms, legs
#walking the street
