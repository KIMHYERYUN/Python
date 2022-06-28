#높은 점수 산출하기
#점수 입력
student_scores = input("Input a list of student scores\n").split()
#학생별 점수 리스트화
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)
print(type(student_scores)) #list
#내림차순 나열하기
student_scores_hightolow = student_scores.sort(reverse=True)
print(student_scores_hightolow)
print(type(student_scores_hightolow))   #NoneType
#제일 높은 점수 산출하기
student_scores_highest = student_scores_hightolow[0]
print(f"The highest score in the class is : {student_scores_highest}")


#다른 방법
print("다른 방법")
#점수 입력
student_scores = input("Input a list of student scores\n").split()
#학생별 점수 리스트화
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)

#제일 높은 점수 산출하기
student_scores_highest = 0
for score in student_scores:
    if score > student_scores_highest:
        highest_score = score
print(f"The highest score in the class is : {student_scores_highest}")


#최고 높은 : max(student_scores)
#제일 낮은 : min(student_scores)