'''
#TODO 1. Flask - app server 및 web application 만들기
    app = Flask(__name__)
    @app.route("/")
    @app.route("/post/<int:index>")
    if  __name__= "__main__":
        app.run(debug=True)
#TODO 2. api url을 통해 data 가져오기 - json : json_object_reason/test.py + post.py 참조
#TODO 3. home 구성
    render_template(index.html, all_post=post_objects)
#TODO 4. index.html - 해당 컨텐츠 반복문 적용 및 링크 - show_post와 parameter : index로 연결
#TODO 5. show_post 구성 - index와 post의 id 일치할 시 requested_post라는 변수가 그 데이터가 되어 보여주는 구성
    render_template("post.html", post=requested_post)
#TODO 6. post.html - 해당 컨텐츠 적용
#TODO 7. 실행 및 테스트

'''