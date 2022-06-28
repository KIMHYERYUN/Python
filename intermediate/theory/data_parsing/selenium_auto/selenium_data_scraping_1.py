#TODO 1. Python 홈페이지의 이벤트 일정 데이터 가져오기
from selenium import webdriver

chrome_driver_path = "C:\projects\chromedriver\chromedriver"
url = "https://www.python.org/"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get(url)
event_times = driver.find_elements_by_css_selector(".event-widget time")
for time in event_times:
    print(time.text)

event_names = driver.find_elements_by_css_selector(".event-widget li a")
for name in event_names:
    print(name.text)

events = {}
for n in range(len(event_times)):
    events[n] = {
        "time": event_times[n].text,
        "name": event_names[n].text
    }
print(events)
'''
{0: {'time': '2022-06-28', 'name': 'PyCon Israel 2022'},
 1: {'time': '2022-06-28', 'name': '(Hybrid) A Deep Dive into Containerized Model Serving with FastAPI'},
 2: {'time': '2022-07-09', 'name': 'PyCon Colombia 2022'}, 3: {'time': '2022-07-11', 'name': 'EuroPython 2022'},
 4: {'time': '2022-08-19', 'name': 'Kiwi PyCon XI'}}
'''