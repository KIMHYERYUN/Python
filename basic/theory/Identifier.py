#식별자(identifier) : 함수, 클래스, 모듈명 등을 총칭
#식별자의 규칙
#공백이나 특수문자 사용불가, 예약어 사용불가

#예약어가 들어있는 keyword모듈 임포트
#모듈 : 자주 사용하는 수식이나 기능 등의 파이썬 파일 - 라이브러리 역할(설치 시 기존내장)
import keyword
#keyword 모듈의 리스트를 불러와서 변수에 대입
#kwlist : 불러오는 함수
python_keyword = keyword.kwlist
print(python_keyword)

#true x - True : 대소문자 구분