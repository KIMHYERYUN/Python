alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


#########버그수정
#####1. 26개 알파벳 이외의 숫자 입력 시 오류현상


if direction == "encode":
    #Encode
    def encode(text,shift):
        #text의 철자 파악 - index 구하기
        cipher_text = ""
        for letter in text:
            idx = alphabet.index(letter)
            new_idx = idx + shift
            #####1. 숫자 초과
            new_idx_upgrade = new_idx % len(alphabet)
            new_letter = alphabet[new_idx_upgrade]
            cipher_text += new_letter
            print(f"The encoded text is {cipher_text}")

    encode(text, shift)

elif direction == "decode":
    #Decode
    def decode(text, shift):
        # text의 철자 파악 - index 구하기
        cipher_text = ""
        for letter in text:
            idx = alphabet.index(letter)
            new_idx = idx - shift
            #####1. 숫자 초과
            new_idx_upgrade = new_idx % len(alphabet)
            new_letter = alphabet[new_idx_upgrade]
            cipher_text += new_letter
            print(f"The encoded text is {cipher_text}")


    decode(text, shift)

else:
    print("You entered the wrong direction.")



###