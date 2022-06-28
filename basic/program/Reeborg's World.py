#reeborg.ca/
#함수 종류 : move(), turn_left(), take(), put(), toss(), build_wall(), pause(), done(),
#think(100), sound(True), World(), UsedRobot(), no_highligt()

#turn_right 함수 정의 - 좌측을 3번돌면 우측을 향함
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

#2*2 영역 한칸씩 갔다가 작은 사각형 만들고 제자리로 돌아오기 - Draw Square
#방법 1 : turn_right 이용 안했을 경우
# turn_left()
# move()
# turn_left()
# turn_left()
# turn_left()
# move()
# turn_left()
# turn_left()
# turn_left()
# move()
# turn_left()
# turn_left()
# turn_left()

#방법 2 : turn_right 이용했을 경우
# turn_left()
# move()
# turn_right()
# move()
# turn_right()
# move()
# turn_right()
# move()



#허들게임
# Reeborg has entered a hurdles race. Make him run the course, following the path shown.
# A robot located at (x, y) = (1, 1) carries no objects.
# The final position of the robot must be (x, y) = (13, 1)

# Easy level
# What you need to know
# The functions move() and turn_left().
# for i in range(1, 7):
#     move()
#     turn_left()
#     move()
#     turn_left()
#     turn_left()
#     turn_left()
#     move()
#     turn_left()
#     turn_left()
#     turn_left()
#     move()
#     turn_left()

#turn_right 이용
# for i in range(1, 7):
#     move()
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()

# Difficulty level
# You may have noticed that your solution has some repeated patterns.
# If you know how to define functions, define a function named jump() and use it to simplify your program.
# def jump():
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()

# huddle_num = int(input("How many huddles?"))
# for문
# for i in range(1, huddle_num+1):
#     jump()
#
# while문
# while huddle_num > 0:
#     jump()
#     #하나씩 이행 후 줄여나감
#     huddle_num -= 1
#     print(huddle_num)


# 깃발이 어디에 놓여있던 간에 도달
# Reeborg has entered a hurdle race, but he does not know in advance how long the race is. Make him run the course, following a path similar to the one shown, but stopping at the only flag that will be shown after the race has started.
# What you need to know
# The functions move() and turn_left().
# The condition at_goal() and its negation.
# How to use a while loop.
# Your program should also be valid for world Hurdles 1.
# The final required position of the robot will be chosen at random.

#목표에 도달하지 않은 경우
#while at_goal() != True:
##while at_goal() == False:
##while not at_goal():
#    jump()


#허들과 벽이 랜덤으로 나오더라도 목표도달
#Reeborg has entered a hurdle race. Make him run the course, following the path shown.
# The position and number of hurdles changes each time this world is reloaded.
# What you need to know
# The functions move() and turn_left().
# The conditions front_is_clear() or wall_in_front(), at_goal(), and their negation.
# How to use a while loop and an if statement.
# Your program should also be valid for worlds Hurdles 1 and Hurdles 2.

#벽이 없는 경우 : move
#벽이 있는 경우 : jump
#목표에 도달하는 경우 : 종료
# while not at_goal():
#     if front_is_clear():
#         move()
#     else:
#     #elif wall_in_front():
#         jump()




#허들의 유형(높이, 위치)가 무작위로 변하는 게임에서 도달하는 게임
#허들의 높이에 따라 jump하는 함수 정의
# def jump():
#     turn_left()
#     #오른쪽에 벽이 있으면 올라가는 move
#     while wall_on_right():
#         move()
#     turn_right()
#     move()
#     turn_right()
#     #앞에 벽이 없으면 내려가는 move
#     while front_is_clear():
#         move()
#     turn_left()

#벽이 없는 경우 : move
#벽이 있는 경우 : jump(n)
#목표에 도달하는 경우 : 종료
# while not at_goal():
#     if front_is_clear():
#         move()
#     else:
#     #elif wall_in_front():
#         jump()