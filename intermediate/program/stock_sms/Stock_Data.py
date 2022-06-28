#TODO 1. - 주식 DATA 가져오기
#주식 API : https://www.alphavantage.co/documentation/

import requests

STOCK_API_URL = "https://www.alphavantage.co/query?"
STOCK_API_KEY = ""
STOCK_NAME = ""


stock_parameter = {
    #필수사항
    "function" : "TIME_SERIES_DAILY",
    "symbol" : STOCK_NAME,
    "apikey" : STOCK_API_KEY,
    #옵션사항 - 데이터 크기
    "outputsize" : "full compact full"
}

stock_response = requests.get(STOCK_API_URL, params=stock_parameter)
stock_data = stock_response.json()

#print(data)

#TODO 2. - 주식 DATA 중 필요한 항목 가져오기 : 어제의 페장가, 그 전날의 폐장가
#################첫번째 방안####################
#모든 날짜의 정보
data_date = stock_data["Time Series (Daily)"]
#전날의 폐장가 구하기
##values 값만 추출
data_value = data_date.values()
##values 값만 추출한 곳에서 값을 사용하려면 list화 필요!!!!!!!!!!!
data_yesterday = list(data_value)[0]
data_yesterday_close = float(data_yesterday["4. close"])

'''
#################두번째 방안####################
#모든 날짜의 정보를 리스트화 : 날짜는 제외하고 value만 가져와서 list화
data_value_list = [value for (key, value) in data.items()]
#print(data_list) #리스트 안에 날짜를 제외한 각 정보가 {}로 묶여있음
data_value_yesterday = data_value_list[0]
data_value_yesterday_close = data_value_yesterday["4. close"]
'''

#전전날의 폐장가 구하기
data_before_yesterday = list(data_value)[1]
data_before_yesterday_close = float(data_before_yesterday["4. close"])

#TODO 3. 전날의 폐장가와 전전날의 폐장과 비교하기 - 절대값(abs)
difference_close = abs(data_yesterday_close - data_before_yesterday_close)
print(data_yesterday_close)
print(data_before_yesterday_close)
print(difference_close)


#TODO 4. 폐장가 비교 비율
difference_close_percentage = round((difference_close / float(data_yesterday_close)) * 100)
print(difference_close_percentage)


#TODO 5. 폐장가 비율이 2이상일 경우 뉴스 가져오기 - print("Get News")
up_down = ""
if difference_close_percentage > 2:
    #print("Get News")
    up_down = "🔺"
else:
    #print("It's normal")
    up_down = "🔻"


#TODO 6. 뉴스 가져오기

NEWS_API = "https://newsapi.org/v2/everything"
NEWS_API_KEY = ""

COUNT_NEWS = 1

news_parameter = {
    #필수
    "apiKey" : NEWS_API_KEY,
    #옵션
    ##검색 키워드 : 정확히 일치하려면 "", +있어야 하는, -없어야 하는, AND/OR/NOT()
    "q" : "google",
    ##검색 시작지점 : 전날
    "from" : f"{list(data_date.keys())[0]}",
    ##언어 : 영어
    "language" : "en",
    ##정렬순서 : 인기순
    "sortBy" : "popularity"
}

news_response = requests.get(NEWS_API, params=news_parameter)
news_data = news_response.json()
#print(news_data)

#TODO 7. 뉴스 중 필요한 항목 가져오기 - Title, url
##오류 : news_data_title = news_data["articles"]["title"] - 리스트 이므로 ["title"] 불가
news_data_count = news_data["articles"][:COUNT_NEWS]

for article in news_data_count:
    formatted_article = f"{STOCK_NAME}: {up_down}{difference_close_percentage}%\nHeadline:{article['title']}.\nBrief: {article['description']}"
    print(formatted_article)

##같은 방법 : formatted_article = [f"{article['title']}.\nBrief: {article['description']}" for article in news_data_count]


#TODO 8. 메세지 보내기

from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = ''
auth_token = ''
client = Client(account_sid, auth_token)
for article in formatted_article:
    message = client.messages \
                    .create(
                         body=article,
                         from_='+18286722158',
                         to='+'
                 )

print(message.sid)

'''
'Meta Data': {
    '1. Information': 'Daily Prices (open, high, low, close) and Volumes',
    '2. Symbol': 'GOOG',
    '3. Last Refreshed': '2022-06-03',
    '4. Output Size': 'Compact',
    '5. Time Zone': 'US/Eastern'
  },
  'Time Series (Daily)': {
    '2022-06-03': {
      '1. open': '2319.8500',
      '2. high': '2327.2900',
      '3. low': '2273.3600',
      '4. close': '2291.2800',
      '5. volume': '1247604'...
'''
