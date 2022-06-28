#initialize : 객체 초기화
#처음 숫자나 변수 등 지정할 수 있음

#생성자를 만들려면 init함수를 사용함
#   속성 초기화
#   처음 실행 시 나타나는 고정값
#class 클래스명:
#   def __init__(self):
#   initialise attributes
#   def __init__(self, attribute1, attribute2...):
#   self(자신의 객체).attribute1 = "초기값"
#   self(자신의 객체).attribute2 = "초기값"
#   print("처음 실행시/객체 생성시 실행되는 출력값)

class Car:
    def __init__(self,seats):
        self.seats = seats

my_car = Car(5)
#my_car.seats = 5


class User:
    def __init__(self, user_id, username):
    # def __init__(self, user_id, username, follower) : follower 생략
        self.id = user_id
        self.username = username
        self.followers = 0
        #속성인 id, username과 변수의 값 user_id, username은 같을 필요는 없으나 권고
        #속성인 followers과 변수 follewer는 0을 기본값으로 설정
        self.following = 0

    #follow 하는 함수 : 자신과 follow하는 사람을 매개변수
    def follow(self, user):
        user.followers += 1
        self.following += 1



#user_1의 객체가 생성되는 순간 user_id, username이 생성
#단, 객체 생성시 속성값 입력

#아래 오류 : TypeError: __init__() missing 2 required positional arguments: 'user_id' and 'username'
# user_1 = User()
# user_1.id = "001"
# user_1.username = "Jay"

#user_1 = User("001", "Jay", 0)
#TypeError: __init__() takes 3 positional arguments but 4 were given
#followers = 0 기본값으로 작성안해도 기본적으로 설정
user_1 = User("001", "Jay")
user_2 = User("002", "Kim")

print(user_1.followers)
#0



#user_1이 user_2를 팔로우했다고 했을 경우
user_2.follow(user_1)
print(user_1.followers) #1
print(user_1.following) #0
print(user_2.followers) #0
print(user_2.following) #1
