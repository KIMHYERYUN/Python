from flask import Flask, render_template
import random
import datetime

app = Flask("__name__")

@app.route("/")
def home():
    random_number = random.randint(1, 100)
    current_year = datetime.datetime.now().year
    #키와 값의 형태로 변수 전달 -> 키를 html에 매칭하여 값을 전달해야 하므로
    return render_template("index.html", num=random_number, year=current_year)


if __name__ == "__main__":
    app.run(debug=True)