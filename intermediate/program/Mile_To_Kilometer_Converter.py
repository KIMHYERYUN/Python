#마일 입력 후 calculate 버튼 클릭 시 변환

from tkinter import *
#윈도우 객체 생성
window = Tk()
#윈도우 사이즈
window.minsize(width=150, height=100)
#윈도우 제목
window.title("Hyeryun's mile to km")
#윈도우 여백
window.config(padx=20, pady=20)


def mile_to_km():
    mile = float(miles_input.get())
    km = round(mile * 1.609)
    kilometer_result_label.config(text=f"{km}")



miles_input = Entry()
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

kilometer_result_label = Label(text="0")
kilometer_result_label.grid(column=1, row=1)

kilometer_label = Label(text="Km")
kilometer_label.grid(column=2, row=1)

calculator_button = Button(text="Calculate", command=mile_to_km)
calculator_button.grid(column=1, row=2)


window.mainloop()



