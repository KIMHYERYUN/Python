print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

#각 이름의 true love 철자 count
#이름을 합하여 소문자로 변형 - 소문자로 해당글자 찾기
total_name = (name1 + name2).lower()
true_t = total_name.count("t")
true_r = total_name.count("r")
true_u = total_name.count("u")
true_e = total_name.count("e")

love_l = total_name.count("l")
love_o = total_name.count("o")
love_v = total_name.count("v")
love_e = total_name.count("e")

true = true_t + true_r + true_u + true_e
love = love_l + love_o + love_v + love_e
#문자열 결합 -> 정수 변환하여야 조건문 적용가능
love_score = int(str(true) + str(love))
#love_score = 10*true + love

if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score >= 40 and love_score <=50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}")