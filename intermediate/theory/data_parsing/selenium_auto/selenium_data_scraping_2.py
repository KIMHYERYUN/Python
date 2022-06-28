from selenium import webdriver
from selenium.webdriver import Keys

chrome_driver_path = "C:\projects\chromedriver\chromedriver"

url = "https://en.wikipedia.org/wiki/Main_Page"
URL="http://secure-retreat-92358.herokuapp.com/"

driver = webdriver.Chrome(executable_path=chrome_driver_path)
'''
driver.get(url)

#두개의 anchor tag 가 나오지만 element로 첫번째만 출력
article_count = driver.find_element_by_css_selector("#articlecount a")

#print(article_count.text)
#6,522,297


#TODO 2. 클릭 동작
#지정 클릭 - href = ""
article_count.click()

#텍스트 링크 클릭 - <a>text</a>
driver.find_element_by_link_text("Mathematics")


#TODO 3. 입력
#검색창 찾기 - 입력값 넣기
search = driver.find_element_by_name("search")
search.send_keys("Python")

#TODO 4. 검색(엔터키)
search.send_keys(Keys.ENTER)

driver.close()
'''



#TODO 5. 실습 - 자동입력
driver.get(URL)

first_name = driver.find_element_by_name("fName")
first_name.send_keys("Hyeryun")

last_name = driver.find_element_by_name("lName")
last_name.send_keys("Kim")

email = driver.find_element_by_name("email")
email.send_keys("90x619@gmail.com")

submit = driver.find_element_by_class_name("btn-block")
submit.click()

####클래스 입력 시 띄어쓰기 확인!! : 여러 클래스로 되어있는 경우이니 일부만 골라서 선택