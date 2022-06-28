#학생들의 키 입력 - 분리
student_heights = input("Input a list of student heights \n").split()
#리스트 생성
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
print(student_heights)

#학생들의 키 합계 구하기
student_heights_sum = sum(student_heights)
print(f"합계: {student_heights_sum}")

#학생들의 키 평균 구하기 - 합계 / 총 개수
#반올림
student_heights_average = round(student_heights_sum / len(student_heights))
print(f"평균: {student_heights_average}")


#다른 방법
print("다른방법")
#학생들의 키 입력 - 분리
student_heights = input("Input a list of student heights \n").split()
#리스트 생성
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
print(student_heights)

#학생들의 키 합계 구하기 - 조건문 이용
#조건문 1
student_heights_sum = 0
for n in range(0, len(student_heights)):
  student_heights_sum += student_heights[n]
  print(n)
print(f"합계: {student_heights_sum}")

#조건문 2
#student_height = 0
#for student_height in student_heights:
#  student_heights_sum += student_height
#print(f"합계: {student_heights_sum}")

#학생들의 수 구하기
student_count = 0
for student in student_heights:
  student_count += 1

#학생들의 키 평균 구하기 - 합계 / 총 개수
#반올림
student_heights_average = round(student_heights_sum / student_count)
print(f"평균: {student_heights_average}")


