#TODO 1. 두개의 속성(이름, 로그인여부)을 가진 클래스 - create_blog_post 함수 사용가능
class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False

def create_blog_post(user):
        print(f"This is {user.name}'s new blog post.")



#TODO 2. 로그인 관리 decorator 생성 - 함수 외 다른인자 전달가능 : *args(limited positional argu), *kwargs(unlimited keyword arguments)
def is_authenticated_decorator(function):
    def wrapper(*args, **kwargs):
        #args의 위치 0 : 첫위치 입력
        #로그인이 될 시 function 실행
        if args[0].is_logged_in == True:
            function(args[0])
    return wrapper


new_user = User("Kim")
new_user.is_logged_in = True
create_blog_post(new_user)


#TODO 3. 예제 ) 자신의 함수이름과 인자 출력
def logging_decorator(function):
    def wrapper(*args, **kwargs):
        print(f"You called {function.__name__}{args}")
        result = function(args[0], args[1], args[2])
        print(f"It returned: {result}")
    return wrapper

@logging_decorator
def a_function(a, b, c):
    return a*b*c

a_function(1, 2, 3)
'''
You called a_function(1, 2, 3)
It returned: 6
'''