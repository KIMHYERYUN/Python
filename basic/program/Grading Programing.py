#학생별 점수 저장된 dictionary
student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99,
  "Draco": 74,
  "Neville": 62,
}
#학생별 등급 저장할 수 있는 dictionary
student_grades = {}
for student_name in student_scores:
    score = student_scores[student_name]
    #등급 기준 :
    if score > 90 :
        student_grades[student_name] = "Outstanding"
    elif score > 80:
        student_grades[student_name] = "Exceeds Expectations"
    elif score > 70:
        student_grades[student_name] = "Acceptable"
    else:
        student_grades[student_name] = "Fail"

print(student_grades)