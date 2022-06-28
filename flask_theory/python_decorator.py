#python decorator function : 기존함수에 함수를 더해서 추가기능 삽입
import time


def delay_decorator_function(function):
    def wrapper_function():
        time.sleep(2)
        #Do something before
        function()
        #Do something after
    return wrapper_function

@delay_decorator_function
def say_hello():
    print("Hello")
#2초후 hello 출력


@delay_decorator_function
def say_bye():
    print("Bye")

def say_greeting():
    print("How are you?")


decorated_function = delay_decorator_function(say_greeting)
decorated_function()


###################################################################################

import time
current_time = time.time()
print(current_time)

def speed_calc_decorator(function):
    def wrapped_function():
      start_time = time.time()
      function()
      end_time = time.time()
      print(f"{function.__name__} run speed : {end_time - start_time}")
    return wrapped_function

@speed_calc_decorator
def fast_function():
    #0부터 10000000까지 증가반복 - 시간delay
    for i in range(10000000):
        i * i

@speed_calc_decorator
def slow_function():
    for i in range(100000000):
        i * i

fast_function()
slow_function()
'''
1655914016.4243078
fast_function run speed: 3.09891676902771s
slow_function run speed: 26.918493509292603s
'''

