#모듈(module) : 프로그래밍의 분할된 기능, 각 파이썬(.py) 확장자
#모듈 내에 함수 존재, 모듈.함수

#import 모듈


#random 모듈
#random(a, b) : a이상 b미만 난수생성
#random 함수
#ranint(a, b) : a이상 b미만 정수 난수 생성
#random() : 0이상 1미만 실수 난수생성
#random() * n : 0이상 n미만 실수 난수생성

import random
#1이상 10미만의 정수 난수생성
randomInteger = random.randint(1, 10)
print(randomInteger)
#0이상 5미만의 실수 난수생성
randomFloat = random.random() * 5
print(randomFloat)
#0이상 100미만 정수 난수생성 - love_score 매김
love_score = random.randint(1, 100)
print(f"Your love score is {love_score}")
#0이상 1미만 정수 난수생성 - 조건문 - 1의 경우 : 머리, 아닐경우 : 꼬리
random_side = random.randint(0,1)
#random_side = random.randint(0,1)
if random_side == 1:
    print("Heads")
else:
    print("Tails")
