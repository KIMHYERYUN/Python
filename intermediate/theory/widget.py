#http://tcl.tk/man/tcl8.6/TkCmd/entry.htm
from tkinter import *

##window
window = Tk()
window.title("Hyeryun's first GUI Program")
window.minsize(width=500, height=500)

##label
#my_label = tkinter.Label(text="I am a label", font=("Arial", 24, "bold"))
my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
#my_label.pack(side="left")
my_label.pack()

#text 수정
my_label["text"] = "New Text"
#속성을 변경할 수 있는 함수
my_label.config(text="New")

##entry : 빈칸 생성
input = Entry(width=10)
#빈칸 위치시키기
input.pack()
#입력값을 가져오기 - get
#print(input.get())


##button
#button 클릭 시 명령 생성 및 적용
def button_click():
    #print("i got clicked")
    #my_label.config(text="Button clicked")
    print(input.get())
    my_label.config(text=input.get())
#오류 : 버튼을 누르기도 전에 이미 실행 - 괄호 없애기
#button = Button(text="Click Me", command=button_click())
button = Button(text="Click Me", command=button_click)

#버튼 놓기
button.pack()


##text 박스
#text 박스 크기
text = Text(height=5, width=30)
#text 커서 지정
text.focus()
#text 안의 고정문 - 다음문장 뒤에 커서 올 수 있도록
text.insert(END, "YOU CAN WRITE DOWN AFTER THIS SENTENCES.")
#첫번째 라인에서 글자 0으로 시작하는 텍스트를 가져옴
print(text.get("1.0", END))
#텍스트 상자 놓기
text.pack()



##spinbox : 수량증가
#스핀박스 크기, 숫자 지정 - 명령 삽입(누를때마다 기록)
def spinbox_click():
    print(spinbox.get())
spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_click)
#스핀박스 놓기
spinbox.pack()



#scale : 스크롤
#스케일 생성, 숫자 지정
def scalebox_click(value):
    print(value)
scale = Scale(from_=0, to=100, command=scalebox_click)
#스크롤 놓기
scale.pack()



#checkbutton : 체크여부 - on/off : 1/0(IntVar라는 클래스 활용)
def checkbutton_click():
    print(checked_state.get())
checked_state = IntVar()
checkbutton = Checkbutton(text="Is on?", variable=checked_state, command=checkbutton_click)
#checked_state.get()
checkbutton.pack()

#radiobutton : 몇 개 중 하나 선택
def radio_click():
    print(radio_state.get())
#체크 상태
radio_state = IntVar()
#체크 옵션 설정
radiobutton_1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_click)
radiobutton_2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_click)
radiobutton_1.pack()
radiobutton_2.pack()




#listbox : 리스트 나열
def listbox_click(event):
    #선택되어있는 것을 가져오기
    print(listbox.get(listbox.curselection()))
listbox = Listbox(height=5)
names = ["Kim", "Hur", "Park", "Lee", "Jung"]
for name in names:
    #인덱스, 넣을글자
    listbox.insert(names.index(name), name)
#리스트에서 선택했을때 신호보내기
listbox.bind("<<ListboxSelect>>", listbox_click)
listbox.pack()

listbox.bind
window.mainloop()