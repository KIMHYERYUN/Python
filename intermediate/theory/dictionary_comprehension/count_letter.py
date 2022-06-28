#글자 수 세기

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"

#리스트화
sentence_split = sentence.split()
print(sentence_split)
#['What', 'is', 'the', 'Airspeed', 'Velocity', 'of', 'an', 'Unladen', 'Swallow?']

#딕셔너리화
sentence_dict = {word:len(word) for word in sentence_split}
print(sentence_dict)
#{'What': 4, 'is': 2, 'the': 3, 'Airspeed': 8, 'Velocity': 8, 'of': 2, 'an': 2, 'Unladen': 7, 'Swallow?': 8}