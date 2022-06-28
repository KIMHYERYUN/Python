#def function_a(something):
    #Do this with something
    #Then do this
    #Finally do this

#def function_b():
    #Do this

#function_a(function_b)
#고차함수 : 함수에 함수를 입력하는 경우 () 생략하고 이름만 전달달

def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2

def calculator(n1, n2, func):
    return func(n1, n2)

result = calculator(1, 2, add)
print(result)