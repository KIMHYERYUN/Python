#출력함수 : print

#"", '' 따옴표로 문자의 시작과 끝을 표시
#""와 '' 순서 상관없음
print("what to print")

print('what to print')
print("print('what to print')")
#print("print("what to print")")
#print 함수는 가까운 ""을 먼저 인지하여 수행되기 때문에
#"print(" 인식 후 what to print라는 코드로 이후에 ")"를 인식
#따라서 what to print라는 코드는 구문오류


#공백설정 : "공백 넣고싶은 간격만큼 spacebar"

#\n : enter 역할
#print는 기본으로 enter 역할
print("Hello")
print("Hello")

print("Hello\n" + "Hello")
