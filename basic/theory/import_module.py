#import : 특정 모듈 가져오기
import moudule_name

#모듈에서 클래스 및 함수 가져오기
from {module} import {class/function}

# *문자는 모두 가져오기
from math import *

#모듈에 별칭 붙이기
import {module} as {module nickname}



#사용자 정의 모듈 만들기
#사용자 정의 모듈 파일(.py)를 만든 후 함수와 같은 내부내용 작성
#import {사용자 정의 모듈 파일명}


#다른 디렉토리에 있는 경우
import importlib, importlib.util
def module_directory(name_module, path):
    P = importlib.util.spec_from_file_location(name_module, path)
    import_module = importlib.util.module_from_spec(P)
    P.loader.exec_module(import_module)
    return import_module

result = module_directory("result", "../inspect_module/test1.py")



#다른 파일에서 클래스를 가져오는 경우
#다른 파일의 클래스(test.py)
class Employee:
    designation = ""
    def __init__(self, result):
        self.designation = result
    def show_designation(self):
        print(self.designation)

class Details(Employee):
    id = 0
    def __init__(self, ID, name):
        Employee.__init__(self, name)
        self.id = \
            name
    def get_Id(self):
        return self.id

#위 파일 가져오기
import importlib, importlib.util
def module_directory(name_module, path):
    P = importlib.util.spec_from_file_location(name_module, path)
    import_module = importlib.util.module_from_spec(P)
    P.loader.exec_module(import_module)
    return import_module
result = module_directory("result", "../Hello/tests.py")
a = result.Employee('Project Manager')
a.show_designation()
x = result.Details(4001, 'Safa')
x.show_designation()
print(x.get_Id())