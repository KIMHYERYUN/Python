import turtle

screen = turtle.Screen()
screen.setup(height=491, width=725)
screen.title("Hyeryun's US Name Game")
#화면에 이미지 넣을준비
image = "blank_states_img.gif"
screen.addshape(image)

#turtle이 그리기
turtle.shape(image)


#데이터 가공
#1. 정답만 있는 리스트 - 정답과 비교하기 위해서
#2. 정답에 대한 x, y축 매칭
import pandas as pd

data = pd.read_csv("50_states.csv")
# data_states = data["state"]
# print(type(data_states))
# data_states_list = []
# data_states_list.append(data_states)
all_states = data.state.to_list()

# 모두 맞추었다는 것을 알기위해 빈리스트 생성 후 채워넣기
guessed_states = []

while len(guessed_states) < 50:

    #정답 입력창 만들기 - 첫번째 대문자로 입력받기(title 함수)
    #정답수 / 문제수 나타내기
    answer_state = screen.textinput(title=f"{len(guessed_states)} / 50, Guess the State",
                                    prompt="What's the state name?").title()

    #exit 입력시 루프 끝내기
    if answer_state == "Exit":
        # 유저가 게임 끝냈을 때까지 맞추지 못한 주의 이름들 csv 파일로 저장
        #방법1
        # missing_states = []
        # for state in all_states:
        #     if state not in guessed_states:
        #         missing_states.append(state)
        #방법2
        missing_states = [state for state in all_states if state not in guessed_states]
        #오류 : missing_states = [state for state in all_states if not in guessed_states] - if 뒤 state 기입
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
        #exit 입력이 확인되면 while 완전 종료


    if answer_state in all_states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        #해당 데이터의 x, y좌표 확인
        data_state = data[data.state == answer_state]
        #해당좌표로 이동
        #오류 : _tkinter.TclError: bad screen distance "34    175.0 - 정수로 변환하지 않아서 생김
        t.goto(int(data_state.x), int(data_state.y))
        #해당좌표에 입력
        #오류 : t.write(data_state.state) - 부가적인 것들도 출력
        #t.write(data_state.state.item())
        t.write(answer_state)
        #맞춘 갯수 확인하기 위해 추가
        guessed_states.append(answer_state)



'''
#화면에 찍는 좌표 알아내기
def get_mouse_click_coor(x, y):
    print(x, y)
turtle.onscreenclick(get_mouse_click_coor)
'''


#코드가 종료되도 남아있는 상태 유지
turtle.mainloop()

#화면이 클릭되면 종료되므로 제거 - 대체. mainloop()
#screen.exitonclick()