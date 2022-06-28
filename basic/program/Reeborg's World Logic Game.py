#미로찾기

#로봇 방향 : 무작위
#로봇 위치 : 무작위
#hint : 오른쪽 가장자리를 따라가기 - 오른쪽, 직진으로 갈 수 없을 경우 왼쪽으로 가면 목표도달

# Reeborg was exploring a dark maze and the battery in its flashlight ran out.

# Write a program using an if/elif/else statement so Reeborg can find the exit.
# The secret is to have Reeborg follow along the right edge of the maze, turning right if it can,
# going straight ahead if it can’t turn right, or turning left as a last resort.

# What you need to know
# The functions move() and turn_left().
# Either the test front_is_clear() or wall_in_front(), right_is_clear() or wall_on_right(), and at_goal().
# How to use a while loop and if/elif/else statements.
# It might be useful to know how to use the negation of a test (not in Python).

# while not at_goal():
#     #오른쪽 벽이 없는 경우 : 오른쪽으로 돌아서 앞의 벽이 없는경우 움직이기 -
#     if right_is_clear():
#         turn_right()
#         move()
#     elif front_is_clear():
#         move()
#     else:
#         turn_left()

#bug : 오른쪽이 항상 비어있는 경우가 발생할 경우(시작하는 위치 사면이 벽이 없음) - 오류수정
# -> 처음 오른쪽이 비어있는 경우 벽을 만들어 주기!
#전방의 벽을 찾고 좌측으로 돌면 그 벽이 우측에 있는 벽이 되는 방법
# while front_is_clear():
#     move()
# turn_left()
#
# while not at_goal():
#     #오른쪽 벽이 없는 경우 : 오른쪽으로 돌아서 앞의 벽이 없는경우 움직이기 -
#     if right_is_clear():
#         turn_right()
#         move()
#     elif front_is_clear():
#         move()
#     else:
#         turn_left()


