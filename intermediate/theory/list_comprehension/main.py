#file1, file2 둘다 들어있는 요소 추출
with open("file1.txt") as file_1:
    file_1_data = file_1.readlines()

with open("file2.txt") as file_2:
    file_2_data = file_2.readlines()

#file1에 있는 원소가 file2에 있다면 추가
#단 결과값이 str이므로 정수변환
result = [int(element) for element in file_1_data if element in file_2_data]

print(result)
#['3\n', '6\n', '5\n', '33\n', '12\n', '7\n', '42\n', '13\n']
#[3, 6, 5, 33, 12, 7, 42, 13]
