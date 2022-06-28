
# ---------------------------- CONSTANTS ------------------------------- #
import math

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    #더이상 진행되지 않게 위젯을 취소함 ----정지
    window.after_cancel(timer_continue)
    #리셋 해야할 것들
    #00:00 만들기 - 캔버스에 형성된 것은 꼭 canvas를 불러와서 수정
    canvas.itemconfig(time_text, text="00:00")
    #title_label = timer 만들기
    timer_label.config(text="Timer")
    #check 박스 리셋
    check_marks.config(text="")
    #여태 진행된 로그 - reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #
#타이머 실행
#별도의 실행함수 만드는 이유 : start 클릭 시 생성되야하므로 start_timer를 사용하기 위함
#추가기능 : 25분 일하고 5분 쉬도록 반복하기
def start_timer():
    #전체적인 절차 카운트 할수있는 변수
    global reps
    #일하는 시간 초로 환산
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_breeak_sec = LONG_BREAK_MIN * 60

    reps += 1
    if reps % 8 == 0:
        #20분 긴 휴식 타이머
        count_down(long_breeak_sec)
        #timer_label 색 바꾸기
        timer_label.config(text="Break", fg=PINK)
        #canvas.config(timer_label, fg=PINK)
    elif reps % 2 == 1:
        #25분 일 타이머
        count_down(work_sec)
        timer_label.config(text="Work", fg=RED)
        #25분 일한 후 체크 - 일한 횟수만큼 체크
        mark = ""
        for work_num in range(int(reps/2)):
            mark += " x "
            check_marks.config(text=mark)
    else:
        #5분 휴식 타이머
        count_down(short_break_sec)
        timer_label.config(text="Break", fg=GREEN)
        #canvas.config(timer_label, fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
#오류 :  GUI 프로그램 내에서 발생 - 누르고 새로고침 되는 이벤트를 계속 주시 - 이런 GUI 프로그램 : EVENT Driven
#메인 루프 내에 또다른 루프 존재하는 경우로 아래 코드는 메인 루프에 도달하지 못함
'''
import time

count = 5
while True:
    time.sleep(1)
    count -= 1
'''

#window.after 함수는 시간 대기 후 실행
def count_down(count):
    # 300 -> 05:00 시간형식으로 표시
    #소수점 존재로 math 함수에서 floor
    count_min = math.floor(count / 60)
    count_sec = count % 60

    #00으로 표시하기
    #if count_sec == 0:   --- int
    #    count_sec = "00"  --- str
    if count_min < 10:
        count_min = f"0{count_min}"
    if count_sec < 10:
        count_sec = f"0{count_sec}"


    # 해당 카운트를 화면에 표시 - 직접 지정
    canvas.itemconfig(time_text, text=f"{count_min}:{count_sec}")
    # 오류 : AttributeError: 'int' object has no attribute 'config'
    # time_text.config(text=f"{count}")

    # 1초 후 대기 후 count, 1씩 감소
    if count > 0:
        global timer_continue
        timer_continue = window.after(1, count_down, count -1)
    #00:00에 도달할 경우
    else:
        start_timer()



# ---------------------------- UI SETUP ------------------------------- #
from tkinter import *
#윈도우 생성
window = Tk()
#타이틀
window.title("Hyeryun's Tomato")
#여백생성 - 윈도우의 배경색
window.config(padx=100, pady=100, bg="YELLOW")



#카운트 다운
#오류 : NameError: name 'canvas' is not defined - canvas 정의된 이후로 생성
#count_down(5)



#라벨 생성
timer_label = Label(text="Timer", font=(FONT_NAME, 50, "bold"))
timer_label.config(bg="YELLOW", fg="GREEN")
#오류 - timer_label.config(bg=YELLOW, fg="Blue") : 변수 또한 ""
timer_label.grid(column=1, row=0)

#전반적인 토마토 사진에 대한 control
#canvas 생성 - 영역크기 설정 - 토마토의 배경색 - 토마토 이미지의 테두리 제거
canvas = Canvas(width=200, height=240, bg="YELLOW", highlightthickness=0)
#canvas 위에 얹어 쓸 것들 표현하기 - canvas.create_...
####이미지의 경우 tkinter 에서 이미지를 먼저 집어와야함
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 110, image=tomato_image)

#canvas를 통해 text  - 0, 0은 좌상단에서 부터 시작하며 숫자가 증가할수록 오른쪽, 아래로 이동
time_text = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 35, "bold"))

#canvas 놓기
canvas.grid(column=1, row=1)



#버튼 생성
start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)


#버튼 기능



#checkbox 생성
#방법1
#check_box = Checkbutton(background="YELLOW")
#check_box.grid(column=1, row=3)

#방법2
check_marks = Label(bg="YELLOW", fg="GREEN")
check_marks.grid(column=1, row=3)








window.mainloop()



#각 위젯에 주변영역 기본 흰배경 참고
#GRID로 나눌경우 정사각형이 아니게 나눌수도 있음