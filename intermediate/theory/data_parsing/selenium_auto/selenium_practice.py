from selenium import webdriver
from selenium.webdriver.common.by import By

AMAZON_URL = "https://www.amazon.com/Durgod-Taurus-Mechanical-Gaming-Keyboard/dp/B07QK16RDQ/ref=sr_1_15?keywords=keychron+red+switch+keyboard&qid=1655793117&sprefix=keychron+red%2Caps%2C420&sr=8-15"
PYTHON_URL = "https://www.python.org/"

chrome_driver_path = "C:\projects\chromedriver\chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get(url=PYTHON_URL)

search_bar = driver.find_element_by_name("q")
print(search_bar.get_attribute("placeholder"))

logo = driver.find_element_by_class_name("python-logo")

#해당 클래스의 링크 가져오기
documentation_link = driver.find_element_by_css_selector(".documentation-widget a")
print(documentation_link.text)

#XPath :경로로 추적 : 트리 꼭대기에서 내려와야함 - 속안에 있는 경우 유용 (단, 첫번째)
bug_link = driver.find_element_by_xpath('//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
print(bug_link.text)



'''
driver.get(url=AMAZON_URL)
price = driver.find_element(by=By.XPATH, value="//*[@id='corePrice_desktop']/div/table/tbody/tr/td[2]/span[1]/span[1]")
print(price.text)
#<selenium.webdriver.remote.webelement.WebElement (session="961fa6f2a901b6d8c728442308516de7", element="75d18093-885a-441d-a683-2dc0b13f7cd0")>

#다양한 속성 포함
price = driver.find_element_by_css_selector("span .a-offscreen")
print(price.text)
'''



driver.quit()