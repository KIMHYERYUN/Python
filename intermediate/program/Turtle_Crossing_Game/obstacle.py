from turtle import Turtle, colormode
import random

OBSTACLE_SPEED = 5
MOVE_INCREMENT = 10

class Obstacle:
    def __init__(self):
        self.all_obstacles = []
        #스피드
        self.obstacle_speed = OBSTACLE_SPEED

    def obstacle_create(self):
        #모양
        obstacle = Turtle("square")
        #사이즈 - 1 기본이 10픽셀
        obstacle.shapesize(1, 3)
        #색깔-랜덤
        colormode(255)
        def random_color():
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            random_color = (r, g, b)
            return random_color
        obstacle.color(random_color())
        obstacle.penup()
        #위치-랜덤 : x축은 모두 300에서 시작, y축 -300~300 범위 내 50간격을 띄어서(거북이가 장애물에서 쉴수있는 공간마련)
        obstacle.setposition(300, random.randrange(-220, 270, 50))
        #방향설정-180
        obstacle.setheading(180)
        self.all_obstacles.append(obstacle)

    def obstacle_move(self):
        for obstacle in self.all_obstacles:
            obstacle.forward(MOVE_INCREMENT)

    #LEVEL UP 시 스피드 증가
    def level_up(self):
        self.obstacle_speed += MOVE_INCREMENT