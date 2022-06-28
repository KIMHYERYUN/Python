import time
import tkinter
from tkinter import *
from tkinter import messagebox
#====================기본변수 생성===============================
import pandas
from pandas import *
import random

BACKGROUND_COLOR = "#C1DEC1"


# ==================단어 가져오기===============================
try:
    # csv 파일 읽어오기 - 임의의 인덱스 설정 - 영어, 한글 가져오기
    # data_dataframe = pandas.read_csv("data/Frequency_language_card.csv")
    # 저장된 데이터에서 가져오기
    data_dataframe = pandas.read_csv("data/words_to_learn.csv")
    # print(type(data_dataframe)) #dataframe
    # print(data_dataframe)
    '''
    # dataframe -> dict 형태로 변환
    data_dict = DataFrame.to_dict(data_dataframe)
    '''
except FileNotFoundError:
    messagebox.showinfo(title="error", message="There is no unknown words-history file.")
    original_data_dataframe = pandas.read_csv("data/Frequency_language_card.csv")
    data_value = original_data_dataframe.to_dict(orient="records")
    #판다스가 읽어올때 record 번호 추가

else:
    #각 열의 값을 가져옴
    data_value = data_dataframe.to_dict(orient="records")
    #{Eng : AAA, KOR : BBB} 로 키 통일됨
    '''
    # 랜덤 인덱스 만들기
    global random_index
    random_index = random.randint(0, len(data_dataframe))
    '''

# ==================단어 저장, 제거===============================
def is_known():
    #목록을 구하고 제거
    data_value.remove(data_problem)
    get_word()
    #목록갯수 줄어듬으로 확인
    print(len(data_value))
    #pandas.DataFrame 을 통해 저장
    data_value_dataframe = pandas.DataFrame(data_value)
    #csv로 저장
    #단, 지속적으로 저장시 index 계속 추가되므로 삭제
    data_value_dataframe.to_csv("data/words_to_learn.csv", index=False)

    get_word()


#문제 가져오기, 뒤집히는 거 홀드, 글자 바꾸기, 3초 후 카드 뒤집기(정답 보여주기)
def get_word():
    #랜덤 문제 가져오기
    global data_problem, flip_timer
    #잠깐 3초 멈춤
    window.after_cancel(flip_timer)
    #카드 뒤집기
    canvas.itemconfig(image_create, image=image_front)
    #문제 가져오기
    data_problem = random.choice(data_value)
    #글자 바꾸기
    canvas.itemconfig(title_text, text="English", fill="black")
    # 각 해당 열의 랜덤 인덱스 가져오기
    word_eng = data_problem["English"]
    canvas.itemconfig(word_text, text=f"{word_eng}", fill="black")
    #3초 후 카드 뒤집기
    window.after(3000, func=turn_card)

'''오류 수정 : 다음을 누를 때와 상관없이 3초 후 카드 뒤집힘'''


#=========================정답확인===========================
def turn_card():
    #카드 뒤집기
    canvas.itemconfig(image_create, image=image_back)
    #해당 문구 변경
    canvas.itemconfig(title_text, text="Korean", fill="white")
    word_kor = data_problem["Korean"]
    canvas.itemconfig(word_text, text=f"{word_kor}", fill="white")


#윈도우 생성
window = tkinter.Tk()
#타이틀
window.title("Hyeryun's Flash Card Game")
#여백
window.config(padx=20, pady=20, bg=BACKGROUND_COLOR)

# 3초의 시간주기
flip_timer = window.after(300, func=turn_card)

#캔버스 생성 - 크기
canvas = Canvas(width=800, height=526)
#이미지 삽입
image_front = PhotoImage(file="images/card_front.png")
image_back = PhotoImage(file="images/card_back.png")
#위치 지정하여 생성 - 크기의 반 (중앙)
image_create = canvas.create_image(400, 263, image=image_front)
#이미지 뒷배경, 선 정리
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)

#이미지 위 텍스트 - 위치 지정
title_text = canvas.create_text(400, 133, text="Title", font=("Arial", 40, "italic"))
word_text = canvas.create_text(400, 263, text="Word", font=("Arial", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

#버튼 만들기
#버튼 이미지 가져오기
image_yes = PhotoImage(file="images/right.png")
image_no = PhotoImage(file="images/wrong.png")
#버튼 생성
button_yes = Button(image=image_yes, highlightthickness=0, command=is_known)
button_no = Button(image=image_no, highlightthickness=0, command=get_word)
#버튼 위치
button_no.grid(column=0, row=1)
button_yes.grid(column=1, row=1)


get_word()


window.mainloop()