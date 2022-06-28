#function(parameter = argument)
#parameter : 데이터 이름
#argument : 데이터 값


#position argument : 위치 인자
#parameter의 위치를 대입

#keyword argument : 키워드 인자
#parameter의 이름을 우선으로 대입

#keyword argument > position argument

def function(a, b, c):
    #Do this with a
    print(a)
    #Then do this with b
    print(b)
    #Finally do this with c
    print(c)

def function(c=1, a=2, b=3):
    # Do this with a
    print(a)
    #Then do this with b
    print(b)
    #Finally do this with c
    print(c)