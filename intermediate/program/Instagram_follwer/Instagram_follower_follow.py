import time

from selenium import webdriver

#TODO 1. 변수 설정
from selenium.common import ElementClickInterceptedException, NoSuchElementException
from selenium.webdriver import Keys

CHROME_DRIVER_PATH = "C:\projects\chromedriver\chromedriver"

INSTA_URL = "https://www.instagram.com/"
INSTA_ID = ""
INSTA_PASSWORD = ""

SIMILAR_ACCOUNT = ""

NUMBER_OF_SCROLL = 10
NUMBER_OF_FOLLOWS = 10

#TODO 2. InstaFollower 클래스 생성
class InstaFollower:
    def __init__(self, driver_path):
        driver = self.webdriver.Chrome(executable_path=driver_path)

    # TODO 3. 로그인 하기
    def login(self):
        self.driver.get(INSTA_URL)
        time.sleep(5)

        username = self.driver.find_element_by_name("username")
        password = self.driver.find_element_by_name("password")

        username.send_keys(INSTA_ID)
        password.send_keys(INSTA_PASSWORD)

        time.sleep(2)
        password.send_keys(Keys.ENTER)


    # TODO 4. 팔로우 찾기
    def find_followers(self):
        self.driver.get(f"http://www.instagram.com/{SIMILAR_ACCOUNT}")
        time.sleep(2)
        followers = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        followers.click()

        time.sleep(2)
        modal = self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div[2]")
        for i in range(1, NUMBER_OF_SCROLLS):
            #javascript 실행 -> execute_script() 사용 --> html + script 받아들임
            #팝업의 높이만큼 상단 스크롤
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)

    # TODO 5. 팔로우 하기
    def follow(self):
        all_buttons = self.driver.find_element_css_selector("li button")
        for button in all_buttons:
            try:
                button.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]')
                cancel_button.click()
        '''
        for follow in range(1, NUMBER_OF_FOLLOWS):
            try:
                follow_button = self.driver.find_element_by_xpath(f'/html/body/div[6]/div/div/div[2]/ul/div/li[{char}]/div/div[2]/button')
                follow_button.click()
                time.sleep(1)
            # TODO 6. 이미 팔로우 한 계정 클릭 시 팝업 - 취소버튼 클릭
            except ElementClickInterceptedException:
                cancel = self.driver.find_element_by_xpath('/html/body/div[7]/div/div/div/div[3]/button[2]')
                cancel.click()
                continue
            except NoSuchElementException:
                continue
        '''


bot = InstaFollower(CHROME_DRIVER_PATH)
bot.login()
bot.find_followers()
bot.follow()