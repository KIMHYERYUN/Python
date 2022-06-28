import time

from selenium import webdriver

#TODO 1. 변수 설정
CHROME_DRIVER_PATH = "C:\projects\chromedriver\chromedriver"

TEST_URL = "https://www.speedtest.net/"
PROMISED_DOWN = 300
PROMISED_UP = 50

TWITTER_URL = "https://twitter.com/"
TWITTER_USERNAME = "gimhyelyeon14"
TWITTER_PASSWORD = ""

#TODO 2. InternetSpeedTwitterBot 클래스 생성
class InternetSpeedTwitterBot:
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(executable_path=driver_path)
        self.up = 0
        self.down = 0

    # TODO 3. 인터넷 속도 구하기
    def get_internet_speed(self):
        self.driver.get(TEST_URL)

        start = self.driver.find_element_by_class_name("start-text")
        start.click()

        time.sleep(100)

        download = self.driver.find_element_by_xpath("//*[@id='container']/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span")
        print(download.text)
        upload = self.driver.find_element_by_xpath("//*[@id='container']/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span")
        print(upload.text)

    # TODO 3. 인터넷 공급사에게 트위보내기
    def tweet_at_provider(self):
        self.driver.get(TWITTER_URL)

        login = self.driver.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[5]/a/div/span/span")
        login.click()

        login_username = self.driver.find_element_by_css_selector(".css-1dbjc4n input")
        login_username.send_keys(TWITTER_USERNAME)

        next_button = self.driver.find_element_by_xpath("//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div")
        next_button.click()

        login_password = self.driver.find_element_by_css_selector(".css-1dbjc4n input")
        login_password.send_keys(TWITTER_PASSWORD)

        login_button = self.driver.find_element_by_xpath("//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div/span")
        login_button.click()


        write = self.driver.find_element_by_css_selector(".DraftEditor-root input")
        tweet = f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"
        write.send_keys(tweet)

        tweet_button = self.driver.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div/div/span/span")
        tweet_button.click()


        time.sleep(5)

        pass



bot = InternetSpeedTwitterBot(CHROME_DRIVER_PATH)
bot.get_internet_speed()
bot.tweet_at_provider()