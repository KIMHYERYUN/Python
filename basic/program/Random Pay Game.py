#입력한 이름 중 랜덤으로 한명 선정하여 식사값 지불할 사람을 뽑아주는 게임

#이름 입력
names_string = input("Give me everybody's names, separated by a comma. \n")
#입력된 이름값 - 분리
names = names_string.split(",")
print(names)
#무작위 선정할 수 있는 모듈인 random
import random
#0부터 입력된 이름길이 중 정수 난수생성 = 뽑힌 사람의 index
#(중요) len(names) 보다 index는 1이 적음
choice_names_index = random.randint(0, len(names)-1)
print(choice_names_index)
#뽑힌 사람의 이름
choice_names = names[choice_names_index]
#출력문구 생성
print(choice_names + " is going to buy the meal today!")
#print(f"{choice_names} is going to buy the meal today!")
