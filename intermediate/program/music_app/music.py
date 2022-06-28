import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from pprint import pprint

##########################노래 SCRAPING#####################################
#입력값 받기 - 날짜
date = input("What's the date you want to travel? (Write down this format : YYYY-MM-DD)")
url = f"https://www.billboard.com/charts/hot-100/{date}"

#데이터 가져오기
response = requests.get(url)
music_data = response.text

#html형식으로 가져오기
soup = BeautifulSoup(music_data, "html.parser")
#print(soup.prettify())

song_names_tags = soup.find_all(name="h3", id="title-of-a-story", class_="a-no-trucate")
#print(song_names_tags)


#\t\n 제거하기
#song_list = []
#for tag in song_names_tags:
#    song_text = tag.getText()
#    song_text_clear = song_text.replace("\n\n\t\n\t\n\t\t\n\t\t\t\t\t","").replace("\t\t\n\t\n", "")
#    song_list.append(song_text_clear)    

song_names = [song.getText().strip() for song in song_names_tags[3:100]]
#한줄에 한개씩 출력하기
pprint(song_names)


#파일만들기
with open(f"song_list_{date}", "w") as file:
    for song in song_names:
        file.write(f"{song}\n")


##########################앱 만들기#####################################

#앱 만들기 - spotify
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id="",
        client_secret="",
        show_dialog=True,
        cache_path="token.txt"
    )
)

#token.txt의 id 반환 함수 적용
user_id = sp.current_user()["id"]


#노래 url 목록 생성
song_uris = []
year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", limit=1, type="track", market="US")
    #print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotipy. Skipped")



#playlist 만들기
new_playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
print(new_playlist)


#playlist에 곡 넣기
sp.playlist_add_items(playlist_id=new_playlist["id"], items=song_uris)
