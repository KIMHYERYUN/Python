#parsing(파싱) : 웹사이트에 포함된 정보 추출하기 위한 첫단계
    #- 로그인 등 정보동의 필요한 곳, (Re)captcha 있는 곳 -> 데이터 스크롤링 x
    #- 상업적 이용 x

    #public api first :
    #윤리적 : 다운될 경우 손해

    #홈페이지 주소 + /robots.txt : 웹사이트를 스크랩하는 봇에게 제공하는 조언 확인(봇이 접근 x 홈페이지, crawl-delay : 재접근 시 시간간격

#BeautifulSoup : HTML, XML과 같은 구조적언어 에서 데이터를 가져오기 위한 파이썬 라이브러리 -
#parser : html.parser로 작동하지 않으면 lxml.parser로 동작시켜봄

from bs4 import BeautifulSoup
import lxml
from gtts import gTTS

with open("website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")
print(soup.title)
#<title>Hyeryun's Personal Site</title>
print(soup.title.string)
#Hyeryun's Personal Site


#html 들여쓰기 적용
print(soup.prettify())

#첫번째 해당 태그 가져오기
print(soup.a)

#모든 컴포넌트 가져오기 - 태그 활용 : 리스트 형태
all_anchor_tags = soup.find_all(name="a")
print(all_anchor_tags)
#[<a href="https://www.appbrewery.co/">Python Data Analysist</a>, <a href="https://angelabauer.github.io/cv/hobbies.html">
# My Hobbies</a>, <a href="https://angelabauer.github.io/cv/contact-me.html">Contact Me</a>]

##태그 내의 글자만 가져오기 - getText 활용
for tag in all_anchor_tags:
    print(tag.getText())

#Python Data Analysist
#My Hobbies
#Contact Me

##태그 내의 링크만 가져오기 - attribute 활용
for tag in all_anchor_tags:
    print(tag.get("href"))

##태그이름 : name
##태그 일부만 가져오기 - attribute or id 등 활용(단, class 이용불가 : reserve 단어로 클래스를 생성할 때만 사용 - class_ 사용)
heading = soup.find(name="h1", id="name")
print(heading)
#<h1 id="name">Hyeryun Kim</h1>

#section_heading = soup.find(name="h3", class="heading")
#오류 : class 불가 --> class 대신 class_ 사용
section_heading = soup.find(name="h3", class_="heading")
print(section_heading)
#<h3 class="heading">Education</h3>
print(section_heading.name)
#h3
print(section_heading.get("class"))
#['heading']




#드릴다운 : 해당되는 조건에 맞게 가져오기(selector="css 기법 해당 태그")
# select : 해당되는 것 모두
# select_one : 해당되는 것 처음 것만
my_url = soup.select_one(selector="p a")
print(my_url)
#<a href="https://www.appbrewery.co/">Python Data Analysist</a>

my_name = soup.select_one(selector="#name")
print(my_name)
#<h1 id="name">Hyeryun Kim</h1>

heading_list = soup.select(selector=".heading")
print(heading_list)