import re

import requests
from bs4 import BeautifulSoup

#사이트에서 데이터 가져오기
response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
movie_data = response.text

#데이터를 html 형태로 가져오기
soup = BeautifulSoup(movie_data, "html.parser")
#print(soup.prettify())

#제목 태그 가져오기
movie_tags_h3 = soup.find_all(name="h3", class_="jsx-[0-9]+")
print(movie_tags_h3)


movie_titles = [movie.getText() for movie in movie_tags_h3]
print(movie_titles)



#리스트 반대순서로 추출
movie_titles_last = movie_titles[::-1]

#마지막부터 처음까지 1 감소방향으로
for n in range(len(movie_titles)-1, 0, -1):
    print(movie_titles[n])


with open("movies.txt", mode="w") as file:
    for movie in movie_titles_last:
        file.write(f"{movie}\n")

