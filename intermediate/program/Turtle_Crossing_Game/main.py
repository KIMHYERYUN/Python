import time
import random
from turtle import Turtle, Screen
from turtle_manager import TurtleManager
from obstacle import Obstacle
from scoreboard import Scoreboard


screen = Screen()
#배경색
screen.bgcolor("white")
#크기
screen.setup(width=600, height=600)
#제목
screen.title("Hyeryun's crossing game!")
#자동화면 갱신 off
screen.tracer(0)


#터틀 객체 생성
player = TurtleManager()
#장애물 객체 생성
obstacle = Obstacle()
#스코어 보더 객체 생성
scoreboard = Scoreboard()


screen.listen()
#함수()는 그 지점에서 실행되기 때문에 () 생략
screen.onkey(fun=player.go_up, key="Up")


is_game_on = True
while is_game_on:
    #타임 지정
    time.sleep(0.1)
    #자동화면 갱신 on
    screen.update()

    #빈번하게 발생 줄이기
    # 방법1 : time.sleep 늘리기
    # 방법2 : 7번중 1번 - 랜덤으로 1이 걸릴 경우에만 장애물 생산
    random_chance = random.randint(1, 8)
    if random_chance == 1:
        #장애물 생성 및 이동
        obstacle.obstacle_create()
        obstacle.obstacle_move()


    #충돌감지 - 각 장애물 거리 비교
    ##오류발생 - for obstacle 시 기존 obstacle.py 내 요소 존재하므로 혼란 - 다른 명칭으로 대체(one)
    for one in obstacle.all_obstacles:
        if one.distance(player) < 20:
            is_game_on = False
            scoreboard.game_over()

    #결승선 도달시 - 처음으로 이동, 레벨업
    if player.success_check():
        player.goto_start()
        obstacle.level_up()
        scoreboard.increase_level()


screen.exitonclick()