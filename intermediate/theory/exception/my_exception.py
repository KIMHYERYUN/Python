##나만의 예외 만들기
'''
raise 에러명("에러설명")
'''

height = float(input("height: "))
weight = int(input("weight: "))

if height > 3:
    #예외발생
    raise ValueError("Human Height should not be over 3 meters.")

bmi = weight / height ** 2
print(bmi)

#height 3초과 입력 시 에러발생
'''
Traceback (most recent call last):
  File "C:\Works\workspace\intermediate\basic\exception\my_exception.py", line 11, in <module>
    raise ValueError("Human Height should not be over 3 meters.")
ValueError: Human Height should not be over 3 meters.
'''