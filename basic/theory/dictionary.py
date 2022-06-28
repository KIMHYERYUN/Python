#{key:value}
#dictionary 내에서 index 대신 key

programing_dictionary = {"python" : "language", "bug" : "error", "function" : "a piece of code that you can easily call over"}
#bug라는 키의 값
print(programing_dictionary["bug"])
#error

#추가
programing_dictionary["loop"] = "Doing again"
print(programing_dictionary)
#{'python': 'language', 'bug': 'error', 'function': 'a piece of code that you can easily call over', 'loop': 'Doing again'}

#수정
programing_dictionary["python"] = "one of language"
print(programing_dictionary)
#{'python': 'one of language', 'bug': 'error', 'function': 'a piece of code that you can easily call over', 'loop': 'Doing again'}

#전체삭제
programing_dictionary = {}
print(programing_dictionary)
#{}
#키의 값 출력
for thing in programing_dictionary:
    print(thing)



