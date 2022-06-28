#beautiful soup : 정적
#selenium : 동적(입력, 클릭, 스크롤 등) 가능 - 자동적 처리가능

#브라우저 설치 : chrome, safari....
#브라우저 드라이버 : 버전에 맞는 것

import selenium
from selenium import webdriver
#webdriver: 크롬 브라우저를 구동하고 자동화된 업무 모두 담당 - 다리역활
chrome_driver_path = "C:\projects\chromedriver\chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://www.amazon.com")
driver.close()  #특정 탭 종료
driver.quit()   #전체 브라우저 종료