from flask import Flask, render_template

app = Flask("__name__")

@app.route("/")
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)


#css 내의 파일은 css자체 경로로 지정되어 있기 때문에 변경 불필요