import time

from selenium import webdriver

chrome_driver_path = "C:\projects\chromedriver\chromedriver"
url = "http://orteil.dashnet.org/experiments/cookie/"

driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get(url)

#TODO 2. 5초간 클릭
contine_game = True
while contine_game:
    cookie = driver.find_element_by_id("cookie")
    cookie.click()
    time.sleep(5000)

    #TODO 2.가격 가져오기
    all_prices = driver.find_elements_by_css_selector("#store b")
    item_prices = []

    #TODO 3. 각 가격을 정수형식으로 변형
    for price in all_prices:
        price_text = price.text
        if price_text != "":
           cost = int(price_text.split("-"[1].strip().replace(",", "")))
           item_prices.append(cost)

    #TODO 4. DICT 만들기 - items : prices
    items = driver.find_elements_by_css_selector("#store div")
    item_ids = [item.get_attribute("id") for item in items]
    cookie_dict = {}
    for n in range(len(item_prices)):
        cookie_dict[item_prices[n]] = item_ids[n]

    #TODO 5. 현재 클릭 수 가져오기
    cookie_click_count = driver.find_element_by_id("cookies")
    cookie_click_num= int(cookie_click_count.split(" ")[0])


    #TODO 6. 상품구매 - 업그레이드
    affordable_upgrades = {}
    for cost, id in cookie_dict.items():
        if cookie_click_num > cost:
            affordable_upgrades[cost] = id

    highest_price_affordable_upgrade = max(affordable_upgrades)
    print(highest_price_affordable_upgrade)
    to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]

    driver.find_element_by_id(to_purchase_id).click()

    store_item_count = driver.find_element_by_id("productPrice0")


    # TODO 7. 5초 대기 - 이후 종료선언 및 초당 갯수
    timeout = time.time() + 5
    five_min = time.time() + 60*5 # 5minutes


    if time.time() > five_min:
        cookie_per_s = driver.find_element_by_id("cps").text
        print(cookie_per_s)
        break