#원하는 열과 행을 입력하면 그자리에 보물을 숨기는 지도 만들기
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

#position = str이므로 int로 변환, int/int = float로 int로 변환 또는 반올림
position_column = int(int(position) / 10)
position_row = int(position) % 10
#position_row = int(position) - position_column 도 가능
#position_column = int(position[0])
#position_row = int(position[1])


#position_column 및 position_row는 index와 -1 차이
#"x"라는 보물 표시 대입
map[position_row-1][position_column-1] = "x"

print(f"{row1}\n{row2}\n{row3}")