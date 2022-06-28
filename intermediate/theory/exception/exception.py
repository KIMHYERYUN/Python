#Error : 오류

#Exception : 예외 발생

#FileNotFoundError : 파일 탐색 실패
#KeyError : dict에 key 존재하지 않음
#IndexError : list에 해당 index 존재하지 않음
#TypeError : 데이터 유형 오류로 실행 불가



#Catching Exceptions : 예외 잡기
#try-except 필수
'''
try : 작동할 코드(그렇지만 그렇지 않은 코드)
except : 오류나 원하는 방식이 아닐경우 실행되는 코드
else: 실패하지 않고 성공했을 때 실행되는 코드
finally : 성공 실패 여부와 상관없이 항상 실행되는 코드
'''

#파일 여부를 모름
#아래 코드 실행 순서
#파일 찾아보기 - 없으므로 첫번째 except 실행(파일 생성, 쓰기) - run
# - dic 키에러로 두번째 except 실행(존재하지 않는다고 함) -new_key -> key로 바꾸고 다시 run - finally 실행

#if~else, try~except 차이 : if~else는 빈번히 발생하는 것


try:
    file = open("a_file.txt")
    #추가로 다른오류 생성 - KeyError
    a_dictionary = {"key":"value"}
    #print(a_dictionary["new_key"])
    print(a_dictionary["key"])
# '''
# except:
#     #FileNotFoundError
#     #파일이 없다면 아래 출력
#     print("There was an error")
#     #새로운 파일 생성
#     file = open("a_file.txt", "w")
#     file.write("BRRRRRRRRRR")
# '''
    ##Too broad exception clause : except 부분 노란줄 표시
    #광범위 : PEP8에 따르면 except 단독 사용 x
    ######a_dictionary의 KeyError가 생기더라도 콘솔에서 에러 미생성 - except가 모든 오류를 잡는다
##따라서 특정 오류 지정할 경우 a_dictionary의 KeyError가 생기면 콘솔에 오류 생성
except FileNotFoundError:
    print("There was an error")
    # 새로운 파일 생성
    file = open("a_file.txt", "w")
    file.write("BRRRRRRRRRR")
#여러 except 형성 가능
# '''
# except KeyError:
#     print("That key does not exist")
# '''
#에러난 부분 출력 가능
except KeyError as error_message:
    print(f"The key {error_message} does not exist.")
#try 구문 성공 시 실행 코드
else:
    content = file.read()
    print(content)
#성공실패 상관없이 파일 닫기
finally:
    #file.close()
    #print("File was closed")
    raise TypeError("This is an error that i made up.")

