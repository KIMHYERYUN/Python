#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

#readlines : 각 줄을 리스트 형태로 저장
#replace : 교체
#strip : 공백 지우기

##key : 각 이름을 readlines을 통해 리스트 형태로 저장하며 나눔

with open("./Input/Names/invited_names.txt") as name:
        #각 이름 불러오기
        #names = name.read()
        #각 이름을 불러와 리스트 저장
        names = name.readlines()
        print(names)
        #['KIM\n', 'PARK\n', 'LEE\n', 'CHOI\n', 'HONG\n', 'HUR\n', 'JUNG\n', 'HA']

with open("./Input/Letters/starting_letter.txt") as letter:
        letter_content = letter.read()
        for name in names:
           #이름 공백 지우기
           stripped_name = name.strip()
           new_letter = letter_content.replace("[name]", stripped_name)
           print(new_letter)
           #새로운 파일을 만들어 new_letter 저장하기
           with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
               completed_letter.write(new_letter)