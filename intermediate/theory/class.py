#클래스 만들기
#class 클래스명
#   do something
#   pass(그냥 지나가기)

#클래스의 객체 만들기
#객체명 = 클래스명()
#속성은 객체와 관련된 변수

class User:
    pass

user_1 = User()
#user_1 객체의 속성 : id, username
user_1.id = "001"
user_1.username = "HyeryunKim"

print(user_1.username)
#HyeryunKim


user_2 = User()
user_2.id = "002"
user_2.username = "JaydenKim"