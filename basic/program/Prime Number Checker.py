#소수인지 여부 확인
#소수 : 1과 자신의 약수를 가지고 있는 숫자

number = int(input("Enter the number that you want to know the prime number."))


def prime_checker(number):
    #소수인지 아닌지 기본값 설정
    prime_is = True
    # 자신의 숫자 - 1까지 나눔
    # 나머지가 0이 나올경우 소수가 아님
    for i in range(2, number):
        if number % i == 0:
           #Not a prime
           prime_is = False
    # 소수의 여부 판단 후 문구 출력
    if prime_is:
        print("{number} is a prime number.")
    else:
        print("{number} is not a prime number.")