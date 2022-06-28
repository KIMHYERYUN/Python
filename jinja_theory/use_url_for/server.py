from flask import Flask, render_template
import requests

app = Flask("__name__")

#TODO 1. index.html - 링크연결 /blog/{num} 데이터를 가져와 blog.html 형식에 데이터를 넣어 app을 만듦 - blog.html 연결
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/blog/<num>")
def get_blog(num):
    print(num)
    blog_url ="https://api.npoint.io/704c06f932b16ec2c902"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)

if __name__ == "__main__":
    app.run(debug=True)