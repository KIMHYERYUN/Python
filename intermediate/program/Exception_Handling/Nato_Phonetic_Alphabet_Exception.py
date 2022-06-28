import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

#data 파일의 각 행 불러오기(iterrows)-index와 row 추출-그 중 row의 각 요소 가져와서 dict 구성
phonetic_dict = {row.letter:row.code for (index, row) in data.iterrows()}
#print(phonetic_dict)

def generate_phonetic():
    #입력값
    word = input("Enter a word: ").upper()
    #입력받은 값 시도
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    #오류날 경우
    except KeyError:
        print("Sorry, only letters in the alphabet please")
        #오류 안날때까지 실행
        generate_phonetic()
    #오류나지 않을경우
    else:
        print(output_list)

generate_phonetic()

