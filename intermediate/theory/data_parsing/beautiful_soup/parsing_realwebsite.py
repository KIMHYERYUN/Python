from bs4 import BeautifulSoup
import requests

#해당 사이트 가져오기
response = requests.get("https://news.ycombinator.com/")
yc_webpage = response.text

#html 형식으로 가져오기
soup = BeautifulSoup(yc_webpage, "html.parser")
#제목해당테그 가져오기 - 처음만
news_title = soup.find(name="a", class_="titlelink")
#print(news_titles)
#<a class="titlelink" href="https://planndu.com/blog/the-simple-way-of-creating-long-lasting-habits/" rel="nofollow">The simple way of creating long-lasting habits</a>

#텍스트 가져오기
news_text = news_title.getText()
#print(news_titles.getText())
#The simple way of creating long-lasting habits

#링크 가져오기
news_link = news_title.get("href")
#print(news_link)
#https://melmagazine.com/en-us/story/boreout-vs-burnout

#추선수 가져오기
news_upvote = soup.find(name="span", class_="score").getText()
#print(news_upvote)
#1 point


##########모두 가져오기 - 1) find -> find_all     2) get  -> for 반복문

#제목에 대한 태그 모든항목
news_titles = soup.find_all(name="a", class_="titlelink")
#추천수에 대한 모든항목 - 리스트에 대한 text를 가져올 수 없어 반복문을 통해 각각 리스트 안에 집어넣음
news_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]
'''
#point 글자 없애고 숫자형식으로 바꾸기
for idx in news_upvotes:
    point = int(news_upvotes[idx].split("")[0])
'''



#제목에 대한 태그 모든항목을 끌어온 것을 반복하여 적용
news_texts = []
news_links = []
for news_tag in news_titles:
    news_text = news_tag.getText()
    news_texts.append(news_text)
    news_link = news_tag.get("href")
    news_links.append(news_link)


print(news_titles)
print(news_upvotes)
print(news_texts)
print(news_links)




#####추천수가 많은 기사 링크, 제목 찾기
largest_upvotes = max(news_upvotes)
print(largest_upvotes)
#426
largest_idx = news_upvotes.index(largest_upvotes)
print(largest_idx)
#27

largest_text = news_texts[largest_idx]
print(largest_text)
#OpenHands

largest_link = news_links[largest_idx]
print(largest_link)
#https://openhands.ai4bharat.org/en/latest/index.html
