
#####4. logo 붙이기
import Cipher_Encoder_Decoder_Art
print(Cipher_Encoder_Decoder_Art.logo)
#from logo import Cipher_Encoder_Decoder_Art
#print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

########기능수정
#####1. 비슷한 함수 합치기 : encode, decode - caesar
#####2. 철자 외 문자를 입력할 경우
#####3. 철자를 encode, decode를 입력할 경우 - 먼저 direction 판단 후 실행
#####4. logo 붙이기
#####5. 재시작 여부 물어보기
#####6. encode, decode 외 입력 시 오류


def caesar(text, shift, direction):
    result = ""
    if direction == "decode":
       shift *= -1
    for letter in text:
        #####2. 철자 외 문자를 입력할 경우
        if letter in alphabet:
           idx = alphabet.index(letter)
           new_idx = idx + shift
           result += alphabet[new_idx]
        else:
           result = "•"

        print(f"Here's the {direction}d result: {result}")

#프로그램 시작 여부 확인
should_start = False
while not should_start:
    #대문자 입력 시 소문자로 변환
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    #####6.encode, decode 외 입력 시 오류
    #encode, decode만 성립하므로 그 외 나머지는 모두 잘못된 답변이므로
    if direction != "encode" and direction != "decode":
        print("Your answer is wrong.")
    else:
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))

        caesar(text, shift, direction)

        restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
        if restart == "no":
            should_start = True
            print("Goodbye")
        elif restart =="yes":
            print("Okay, restart the program.")
            should_start = False
        else:
            print("Your answer is wrong.")


