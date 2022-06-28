import pandas as pd

student_scores = {"student":["KIM", "PARK", "HUR"]
                  ,"score":[90, 85, 79]}

import pandas

student_scores_dataframe = pd.DataFrame(student_scores)
print(student_scores_dataframe)
'''
  student  score
0     KIM     90
1    PARK     85
2     HUR     79
'''

for (key, value) in student_scores_dataframe.items():
    print(key)
    print(value)
'''
student
0     KIM
1    PARK
2     HUR
Name: student, dtype: object
score
0    90
1    85
2    79
Name: score, dtype: int64
'''


#데이터프레임의 각 행을 가져옴
for (index, row) in student_scores_dataframe.iterrows():
    print(row)
    print(row.student)
    print(row.score)
'''
student    KIM
score       90
Name: 0, dtype: object
student    PARK
score        85
Name: 1, dtype: object
student    HUR
score       79
Name: 2, dtype: object
'''
'''
KIM
90
PARK
85
HUR
79
'''