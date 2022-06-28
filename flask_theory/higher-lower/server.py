import random

from flask import Flask

#TODO 1. 랜덤 숫자 지정하기
random_number = random.randint(0, 9)
print(f"random_number is {random_number}")

#TODO 2. FLASK APPLICATION 생성
app = Flask(__name__)

#TODO 3. 홈페이지 만들기
@app.route('/')
def home():
    return "<h1 style='text-align:center'>Guess the number from 0 to 9!</h1>" \
           "<img src='https://media.giphy.com/media/fAo1Tv1OGE6AQZ2s0T/giphy.gif' style='display:block; margin:0px auto;'/>"

@app.route('/<int:guess>')
def guess_number(guess):
    if guess > random_number:
        return "<h1 style='text-align:center'>Too high, try again!</h1>" \
               "<img src = 'https://media.giphy.com/media/3ov9jUep4j57U4RtMk/giphy.gif'  style='display:block; margin:0px auto;'/>"
    elif guess < random_number:
        return "<h1 style='text-align:center'>Too low, try again!</h1>" \
               "<img src = 'https://media.giphy.com/media/9oHV6GtmzHjBQ72RuW/giphy-downsized-large.gif'  style='display:block; margin:0px auto;'/>"
    else:
        return f"<h1 style='text-align:center'>Congratulation, you're right. The number is {guess_number}.</h1>" \
               "<img src = 'https://media.giphy.com/media/3o6fJ1BM7R2EBRDnxK/giphy.gif'  style='display:block; margin:0px auto;'/>"

#TODO 4. PYCHARM에서도 제어
if __name__ == "__main__":
    app.run(debug=True)


app.close()