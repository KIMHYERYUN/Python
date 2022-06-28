import time

THEME_COLOR = "#375362"
from tkinter import *
from quiz_brain import QuizBrain

class QuizInterface:
    #quiz_brain이라는 클래스 가져오기 - 객체 생성
    #quiz_brain에서의 QuizBrain의 데이터를 넣을 수 있음
    def __init__(self, quiz_brain : QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Hyeryun's Quiz Game!")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        #점수 라벨 형성
        self.score_label = Label(text="Score:0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        #문제판 생성
        self.canvas = Canvas(width=300, height=250, bg="white")
        #줄바꿈 추가(상자크기 설정)
        self.question_text = self.canvas.create_text(150, 125, width=280, text="question", fill=THEME_COLOR,
                                                     font=("Arial", 15, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        #버튼 생성
        true_image = PhotoImage(file="images/true.png")
        false_image = PhotoImage(file="images/false.png")
        self.button_true = Button(image=true_image, highlightthickness=0, command=self.true_passed)
        self.button_false = Button(image=false_image, highlightthickness=0, command=self.false_passed)
        self.button_true.grid(row=2, column=0)
        self.button_false.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        # 두번째부터 다음 질문 넘어갈 시 흰배경 설정
        self.canvas.config(bg="white")
        #다음 질문이 있을경우
        if self.quiz.still_has_questions():
            #점수 업데이트
            self.score_label.config(text=f"Score:{self.quiz.score}")
            #quiz_brain 객체에 제공되는 메소드 사용가능
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="The End of the quiz.")
            #버튼 지우기
            self.button_true.config(state="disabled")
            self.button_false.config(state="disabled")

    def true_passed(self):
        #정답 확인
        is_right = self.quiz.check_answer("True")
        #정답 확인 후 피드백
        self.give_feedback(is_right)

    def false_passed(self):
        #정답 확인
        is_right = self.quiz.check_answer("False")
        #정답 확인 후 피드백
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        #정답이면 배경색 변경
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        #정답을 알려주고 대기시간 설정 - 단, window tkinter는 정지시킨 후
        #오류 : self.get_next_question() - () 삭제
        self.window.after(1000, self.get_next_question)
