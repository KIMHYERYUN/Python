#TODO 1. HTML 파일 rendering - templates 폴더 안에
'''
from flask import render_template

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)
'''

#TODO 2. 이미지 정적 파일 rendering - static 폴더 안에
#홈페이지 내 inspect > console > error message: 또는 pycharm 콘솔 화면 출력
# error message : 이미지, css 파일 - Failed to load resource: the server responded with a status of 404 (NOT FOUND) -








