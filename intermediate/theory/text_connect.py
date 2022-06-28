#파일 열기 - 읽기 - 출력 - 닫기
#파일 쓰기할 경우 파일의 형태 확인 : 읽기전용, 읽쓰기 가능한지 파악 - mode 3가지 : a(append), w(write), r(read)
#닫는 이유 : 할당된 리소스 제거 - 인터넷 탭과 같이 열려있으면 사용하기에는 편하나 저장공간 할당


#방법1
#파일 열기
file = open("text_connect.txt")
#파일 읽기
content = file.read()
#파일 출력
print(content)
#파일 닫기
file.close()


#방법2
#파일 열기
with open("text_connect.txt") as file:
    # 파일 읽기
    content = file.read()
    # 파일 출력
    print(content)
    # 파일 닫기
    file.close()


#파일쓰기
'''
with open("text_connect.txt") as file:
    # 파일 쓰기
    file.write("I want to write...")
    #오류 : io.UnsupportedOperation: not writable - 읽기전용 
'''


with open("text_connect.txt", mode="w") as file:
    # 파일 쓰기
    file.write("I want to write...")
    #오류 : io.UnsupportedOperation: not writable - 읽기전용


#파일이 존재하지 않으면 파일이 생성됨
with open("text_connect_new.txt", mode="w") as file_new:
    file_new.write("New file is created!")