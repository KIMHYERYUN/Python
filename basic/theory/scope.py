#Local scope(지역변수) : 내부에서만 사용
#Global scope(전역변수) : 외부에서 사용(파일 내부에서 어디든 사용가능)
#Global Constant(전역상수) : pi = 3.14159 등 변경되지 않음, 또한 대문자 사용
#PI, URL, TWITTER_HANDLE

#if, while, for 콜론과 들여쓰기가 있는 모든 코드블록은 지역변수를 만드는 것으로 간주하지 않는다


def drink_potion():
    potion_strength = 2
    print(potion_strength)
drink_potion()
#2

potion_strength = 1
print(potion_strength)
#1

#전역변수 수정하기 : global 붙이기 또는 return 사용
def drink_potion():
    global potion_strength
    potion_strength += 1
    print(potion_strength)
drink_potion()

def drink_potion():
    print(potion_strength)
    return potion_strength + 1
drink_potion()


#player_health 전역변수로 함수 내에서 사용
player_health = 10

def player():
    sports_score = 5
    print(player_health)
player()
#10


stadium = 8

def sport():
    def play():
        power = 5
        print(stadium)

#play 함수 오류 : sport 내부 함수에서만 사용가능,
#play()



#Block scope : 파이썬은 가지고 있지 않다
game_level = 3
enemies_1 = ["Skeleton", "Zombie", "Alien"]
if game_level < 5:
    new_enemy_1 = enemies_1[0]
print(new_enemy_1)
#오류를 나타내지 않는다 : "Skeleton"

#단, 함수를 정의하였을 경우
def create_enemy():
    enemies_2 = ["Shrek", "Purin", "Zerg"]
    if game_level < 5:
        new_enemy_2 = enemies_2[0]
#print(new_enemy_2)
#오류를 나타냄
