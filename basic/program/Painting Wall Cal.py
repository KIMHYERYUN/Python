# ou are painting a wall.
# The instructions on the paint can says that 1 can of paint can cover 5 square meters of wall.
# Given a random height and width of wall, calculate how many cans of paint you'll need to buy.

# number of cans = (wall height + wall width) ÷ coverage per can.
#
# But because you can't buy 0.6 of a can of paint, the result should be rounded up to 2 cans.

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
paint_coverage = int(input("How much 1 can of paint can cover 5 square meters of wall?"))


#올림 함수인 ceil 사용하기 위한 모듈
import math

def paint_calc(height=test_h, width=test_w, cover=paint_coverage):
    number_cans = math.ceil((test_h + test_w) / paint_coverage)
    print(f"You will need {number_cans} cans of paint.")


paint_calc(height=test_h, width=test_w, cover=paint_coverage)
