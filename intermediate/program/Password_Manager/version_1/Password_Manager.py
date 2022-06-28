#tkinter의 모든 클래스와 상수만
from tkinter import *
#messagebox는 클래스가 아니기때문에 별도  - 별도의 모듈과 코드임
from tkinter import messagebox
from random import *
#클립보드 - 자동복사
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generate():
    password_number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    password_symbol = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")"]
    password_letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    password_list = []

    #랜덤갯수 추출
    password_number_count = randint(0, len(password_number))
    password_symbol_count = randint(0, len(password_symbol))
    password_letter_count = randint(0, len(password_letter))
    #오류 :     password_number_count = randint(0, len(password_number))
    #from random import *일 경우, random.randint 오류


    #랜덤갯수 만큼 랜덤으로 추출
    for num in range(password_number_count):
        password_list.append(choice(password_number))

    for sym in range(password_symbol_count):
        password_list.append(choice(password_symbol))

    for char in range(password_letter_count):
        password_list.append(choice(password_letter))



    #리스트를 랜덤으로 배치
    shuffle(password_list)

    #리스트 문자열로 변환
    random_password = ""
    for char in password_list:
        random_password += char

    # 다른 방법 ------ 단축
    '''
    password_number_random = [choice(password_number) for _ in range(randint(0, len(password_number)))]
    password_symbol_random = [choice(password_symbol) for _ in range(randint(0, len(password_symbol)))]
    password_letter_random = [choice(password_letter) for _ in range(randint(0, len(password_letter)))]
.
    password_list = password_number_random + password_symbol_random + password_letter_random
    shuffle(password_list)

    #join함수 : tuple = ("a", "b", "c") | ["a", "b", "c"]   "#".join(tuple) -> a#b#c
    random_password = "".join(password_list)
    '''


    #생성된 비밀번호 출력
    print(f"{random_password}")
    #오류 : 입력되지 않음 - 이유는 기초 text가 없음 password_input.config(text=f"{random_password}")
    password_input.insert(0, random_password)
    #패스워드 생성 시 자동 복사
    pyperclip.copy(random_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
#입력된 값 txt에 저장하기
def save():
    #입력값 가져오기
    website = website_input.get()
    email_name = email_name_input.get()
    password = password_input.get()

    #경고창 만들기 - 비어있는경우
    if website == "" or email_name == "" or password == "":
    #if len(website) == 0 or len(email_name) == 0 or len(password) == 0:
        messagebox.showinfo(title="Empty", message="Please. don't leave any fields empty!")

    else:
        #messagebox 넣기 - ok, cancel 연결
        is_ok = messagebox.askokcancel(title="Check", message=f"These are the details entered: \nWebsite: {website} "
                                                      f"\nEmail/Username: {email_name} \nPassword: {password}"
                                                      f"\nIs it okay to save?")
        if is_ok:
            with open("password_data.txt", "a") as data_file:
                data_file.write(f"{website} | {email_name} | {password} \n")
                #저장이 되면 빈칸의 내용 삭제
                website_input.delete(0, END)
                email_name_input.delete(0, END)
                password_input.delete(0, END)





#---------------------------- UI SETUP -------------------------------

#윈도우 생성
window = Tk()
#윈도우 타이틀
window.title("Hyeryun's Password Manager")
#여백
window.config(padx=50, pady=50)


#이미지 넣기
#canvas 생성 - 크기, 선
canvas = Canvas(width=200, height=200, highlightthickness=0)
#이미지 삽입
password_image = PhotoImage(file="logo.png")
#오류 : IndexError: tuple index out of range - 코드는 튜플을 받고있기에 x, y의 위치 필요
#canvas.create_image(width=200, height=200, image=password_image)
canvas.create_image(100, 100, image=password_image)

canvas.grid(column=1, row=0)


#라벨넣기

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

email_name_label = Label(text="Email/Username:")
email_name_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)



# 입력창 넣기 - 커서넣기
website_input = Entry(width=35)
website_input.grid(column=1, row=1, columnspan=2)
website_input.focus()

email_name_input = Entry(width=35)
email_name_input.grid(column=1, row=2, columnspan=2)
#기본값 설정시
#email_name_input.insert(0, "hyeryun's email.com")

password_input = Entry(width=21)
password_input.grid(column=1, row=3)


#버튼 생성
generate_button = Button(width=14, text="Generate Password", command=password_generate)
generate_button.grid(column=2, row=3)

add_button = Button(width=36, text="Add", command=save)
add_button.grid(column=1, row=4, columnspan=2)




window.mainloop()
