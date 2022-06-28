#fnctions : inputs/functionality/output
#functions are first-class objects(1급 객체-자신이 인자로 사용가능), can be passed around as arguments(int/string/float etc..)
#Nested Functions : Function in Function

def outer_function():
    print("outer")
    def inner_function():
        print("inner")
    inner_function()

#inner_function() : 오류
outer_function()
#outer
#inner


#functions can be returned from other functions
def outer_function():
    print("outer")
    def inner_function():
        print("inner")

    return inner_function

nested_function = outer_function()
#outer_function 실행 - outer 출력 - inner_function 실행하지 않고 그 상태로 반환
nested_function()
#반환된 것을 실행 - inner 출력

##() : 실행 | 없으면 실행 전