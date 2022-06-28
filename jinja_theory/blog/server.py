#TODO. FLASK로 애플리케이션 생성하고 홈페이지 주소 전달 - API를 통해 데이터를 가져와 JSON을 통해 표준 데이터 전송 - JINJA를 통해 PYTHON 코드를 HTML로 전달 -
import requests
from flask import Flask, render_template

#TODO 1.Flask를 통해 app, 홈페이지 주소 및 html 연결
app = Flask("__name__")

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/blog")
def blog():
    blog_url ="https://api.npoint.io/704c06f932b16ec2c902"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)

if __name__ == "__main__":
    app.run(debug=True)