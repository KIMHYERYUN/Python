import time
from selenium import webdriver
from selenium.common import NoSuchElementException

chrome_driver_path = "C:\projects\chromedriver\chromedriver"
url = "https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=103588929&keywords=python%20developer&location=%EB%8C%80%ED%95%9C%EB%AF%BC%EA%B5%AD%20%EC%84%9C%EC%9A%B8"

driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get(url)

login_button = driver.find_element_by_class_name("btn-secondary-emphasis")
login_button.click()

#다음페이지 로딩 대기시간
time.sleep(5)


input_id = driver.find_element_by_id("username")
input_id.send_keys("90x619@gmail.com")

input_password = driver.find_element_by_id("password")
input_password.send_keys("#########")

submit_button = driver.find_element_by_css_selector(".login__form_action_container button")
submit_button.click()

'''
#TODO 2. 저장 + 팔로우
save_button = driver.find_element_by_xpath("/html/body/div[5]/div[3]/div/div[1]/div[1]/div/div[1]/div/div/div[1]/div[3]/div/button")
save_button.click()
follow_button = driver.find_element_by_css_selector(".jobs-company__box button")
follow_button.click()

driver.execute_script("window.history.go(-1)")

    
#TODO 3. 지원하기

apply_button = driver.find_element_by_css_selector(".artdeco-button__text")
apply_button.click()
phone_input = driver.find_element_by_css_selector(".urn:li:fs_easyApplyFormElement:(urn:li:fs_normalized_jobPosting:3129128249,60253797,phoneNumber~nationalNumber)")
phone_input.send_keys("010")
submit_apply = driver.find_element_by_class_name("artdeco-button__text")
submit_apply.click()
'''



#TODO 4. 전체 지원하기
all_listings = driver.find_elements_by_css_selector(".job-card-container--clickable")

#TODO 4-1. 전체 리스트 불러오기
for listing in all_listings:
    print("called")
    listing.click()
    time.sleep(1)

    #TODO 4-2. 지원버튼 클릭하기
    try:
        apply_button = driver.find_element_by_css_selector(".jobs-s-apply button")
        apply_button.click()
        time.sleep(1)

        #TODO 4-3. 전화번호 input - 없을경우
        phone = driver.find_element_by_class_name("fb-single-line-text__input")
        if phone.text == "":
            phone.send_keys("010")

        complete_button = driver.find_element_by_css_selector("footer button")

        #TODO 4-4. 지원건너띌 상황 정의 - SUBMIT BUTTON 다음 NEXT가 있는 경우
        if submit_button.get_attribute("data-control-name") == "continue_unify":
            close_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
            close_button.click()
            time.sleep(1)
            discard_button = driver.find_elements_by_class_name("artdeco-modal__confirm-dialog-btn")[1]
            discard_button.click()
            print("Complex application, skipped.")
            continue
        else:
            submit_button.click()


        #TODO 4-3. 지원완료 팝업창 종료
        time.sleep(2)
        close_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
        close_button.click()

    #TODO 4-4. 셀레니움 요소를 하나도 찾이 못할 때 예외발생
    except NoSuchElementException:
        print("No application button. so skipped")
        continue


    time.sleep(5)
    driver.quit()