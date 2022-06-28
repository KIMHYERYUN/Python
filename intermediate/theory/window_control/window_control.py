import time

from selenium import webdriver

chrome_driver_path = "C:\projects\chromedriver\chromedriver"
url = ""

driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get(url)

#TODO 1. 각 창 식별 : 모든 창을 가져오기 - 리스트형
driver.window_handles

#TODO 2. 첫번째 창의 인덱스 = 0
base_window = driver.window_handles[0]

#TODO 3. 팝업 뜬 새창의 인덱스 순차적 증가 = +1
popup_window = driver.window_handles[1]

#TODO 4. 포커스 전환 : popup창으로 전환
driver.switch_to.window(popup_window)

#TODO 5. 현재 창 확인
print(driver.title)

#TODO 6. 지연시간 - 봇 감지하여 막히는 일 방지
time.sleep(10)

#TODO 7. 예외처리 - NoSuchElementException(해당 요소 안나타날 시) / ElementClickInterceptedException(버튼이 팝업에 가려지는 경우)