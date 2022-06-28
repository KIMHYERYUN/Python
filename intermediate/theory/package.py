#클래스 삽입 - 객체생성 - 객체의 값 추가 - 속성변경
from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Sports name", ["Soccer", "Tennis", "Taekwondo"])
table.add_column("Type", ["Ball", "Ball", "Body"])
print(table)

# +-------------+------+
# | Sports name | Type |
# +-------------+------+
# |    Soccer   | Ball |
# |    Tennis   | Ball |
# |  Taekwondo  | Body |
# +-------------+------+

#Object Attributes : 객체의 속성
#현재 속성을 확인하고 변경할 수 있음
print(table.align)
#{'base_align_value': 'c', 'Sports name': 'c', 'Type': 'c'}

#좌측정렬 = "L" 대문자 불가, left의 "l"
table.align = "l"
print(table)
# +-------------+------+
# | Sports name | Type |
# +-------------+------+
# | Soccer      | Ball |
# | Tennis      | Ball |
# | Taekwondo   | Body |
# +-------------+------+
