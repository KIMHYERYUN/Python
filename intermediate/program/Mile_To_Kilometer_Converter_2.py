#마일 입력 후 calculate 버튼 클릭 시 변환

from tkinter import *
#윈도우 객체 생성
window = Tk()
#윈도우 사이즈
window.minsize(width=300, height=100)
#윈도우 제목
window.title("Hyeryun's mile to km")
#윈도우 여백
window.config(padx=20, pady=20)

#text 입력상자 만들기
input = Entry()
input.grid(column=1, row=0)

#label 상자 만들기
label_1 = Label(text="Miles")
label_1.grid(column=2, row=1)


#label 상자 만들기
km = 0
label_2 = Label(text=f"is equal to {km} km")
label_2.grid(column=0, row=1)

#button 만들기
def button_click():
    # 변환 - 소수 및 올림
    mile = float(input.get())
    km = round(mile * 1.609)
#    convert_mile = int(input.get()) * 1.609344
    label_2.config(text=f"is equal to {km} km")
button = Button(text="Calculate", command=button_click)
button.grid(column=1, row=2)



window.mainloop()



