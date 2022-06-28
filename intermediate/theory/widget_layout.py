#Layout Manager : 위젯 배치하는 방법

#아래 3가지를 이용해 놓여야 화면에 표시할 수 있음
#pack : 다음 줄에 배치, side="left"를 사용하면 한줄에 붙어서 나옴 : 위치를 명시하기 어려움(줄로 위치배치할 수 있음)
#place : x,y축을 가지고 위치 배치 : 많이 존재할 경우 복잡
#grid : column, row를 통해 표 이용

#grid, pack 같이 사용 불가


#padding : 여백 설정
#padx : 가로 여백, pady : 새로 여백



from tkinter import *


def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)


window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
#윈도우 여백 설정
window.config(padx=100, pady=200)

#Label
my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label.config(text="New Text")
my_label.grid(column=0, row=0)
#여백 설정 - config 설정관련 함수
my_label.config(padx=50, pady=50)

#Button
button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

new_button = Button(text="New Button")
new_button.grid(column=2, row=0)

#Entry
input = Entry(width=10)
print(input.get())
input.grid(column=3, row=2)









window.mainloop()