#TODO. FLASK로 애플리케이션 생성하고 홈페이지 주소 전달 - API를 통해 데이터를 가져와 JSON을 통해 표준 데이터 전송 - JINJA를 통해 PYTHON 코드를 HTML로 전달 -
import requests
from flask import Flask, render_template

#TODO 1.Flask를 통해 app, 홈페이지 주소 및 html 연결
app = Flask("__name__")

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/guess/<name>")
def guess(name):
    #TODO 2.API를 통해 데이터 가져옴
    gender_url = f"https://api.genderize.io?name={name}"
    gender_response = requests.get(gender_url)

    age_url = f"https://api.agify.io?name={name}"
    age_response = requests.get(age_url)

    #TODO 3.JSON 데이터 표준구조로 전송
    gender_data = gender_response.json()
    age_data = age_response.json()

    #TODO 3. JINJA를 통해 PYTHON 코드 -> HTML 적용
    gender = gender_data["gender"]
    age = age_data["age"]

    return render_template("index.html", name=name, age=age, gender=gender)

if __name__ == "__main__":
    app.run(debug=True)