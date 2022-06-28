#TKinter 모듈 : 윈도우 창, 레이블, 버튼, 문자입력, 반응, 프로그램 디자인 등

#GUI : Graphical User Interface

#모듈 삽입
import tkinter
#윈도우 생성
window = tkinter.Tk()
#윈도우 명칭
window.title("Hyeryun's Window")
#최소크기 설정
window.minsize(width=500, height=300)


#Label - 생성하고 배치를 해야 화면에 표시됨
#라벨 생성
my_label = tkinter.Label(text = "I am a label", font=("Arial", 24, "bold"))
#배치 선정 - 화면중앙
my_label.pack()
#화면 아래
my_label.pack(side="bottom")
#화면 중앙
my_label.pack(expand=True)

#윈도우 화면고정 - 입력 및 반응 등 유지
window.mainloop()







