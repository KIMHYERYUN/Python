#TODO : 데이터를 가져와서 객체로 묶는이유!!! : 데이터의 접근성도 쉬워지며 다루기 용이함
import requests
from post import Post

posts = requests.get("https://api.npoint.io/704c06f932b16ec2c902").json()
post_objects = []
for post in posts:
    post_obj = Post(post["id"], post["title"], post["subtitle"], post["body"])
    post_objects.append(post_obj)

print(post_objects)
'''
[<post.Post object at 0x0000022C576C0550>, <post.Post object at 0x0000022C576C0580>, <post.Post object at 0x0000022C576C0520>, <post.Post object at 0x0000022C576C0A60>]
'''

for i in post_objects:
    print(i)
    print(i.__dict__)
    #객체는 각 인덱스 또는 키의 값으로 데이터의 내용 가져옴
'''
<post.Post object at 0x0000022C576C0550>
<post.Post object at 0x0000022C576C0580>
<post.Post object at 0x0000022C576C0520>
<post.Post object at 0x0000022C576C0A60>

{'id': 1, 'title': "World of 'hanji' unfolds in southern Italian city of Bari",
 'subtitle': "A colorful 'hanji' wonderland has unfolded in the Italian port city of Bari.",
 'body': "The exhibition, 'Hanji: Paper of Life,' which runs until July 25 at a museum that is housed within the massive 13th-century fortress, Castello Svevo, introduces the traditional Korean paper made with the inner bark of the mulberry tree from its centuries-old production process to its bright-colored contemporary paper handicrafts. The paper is also known for its durability due to its extremely low impurities. It uses mulberry bark without any other additives, which is boiled with lye solely made from natural plant ashes to remove any non-cellulosic elements."}
{'id': 2, 'title': 'Yoon angered by police releasing unapproved reshuffle announcement',
 'subtitle': 'Infighting between police, interior ministry blamed for release of unapproved draft',
 'body': "President Yoon Suk-yeol lashed out at the Korean National Police Agency on Thursday for releasing unapproved documents regarding a police reshuffle before it had been finalized, saying it is either 'a disturbance of national discipline' or 'a nonsensical error' by government officials.'I picked up the story from a news article and looked it up to find out what had actually happened. I figured out that something absurd happened,' Yoon told reporters referring to the incident. 'Police released the list of their own recommendations for the reshuffle, which had yet to be confirmed because it required approval first from the interior ministry and then the president. This is nonsense and equivalent to a disturbance of national discipline as the draft of the list was released.'"}
{'id': 3, 'title': "SpaceX's plan to launch Starlink service in Korea next year draws mixed reactions",
 'subtitle': "Consumers and experts have differed on SpaceX's latest announcement of its plan to start offering satellite internet service using Starlink in Korea next year.",
 'body': "While consumers have remained skeptical about demand for the service in Korea, which already has the world's fastest average internet connection speeds, experts mentioned its commercial potential, urging authorities to brace for the medium- to long-term impacts of foreign companies on Korea's sovereignty over telecommunication services. According to the official website of Starlink, Thursday, Korea is categorized as a country where its satellite internet service is 'coming soon,' due to 'pending service coverage or regulatory approval.'This is the first time for SpaceX to specify when it will launch Starlink service in Korea."}
{'id': 4, 'title': 'I.Seoul.U city slogan to be scrapped',
 'subtitle': 'Seoul Metropolitan Government plans to introduce more appealing, catchier slogan to attract international tourists and foreign investment',
 'body': "Since January this year, Seoul Metropolitan Government has been working on a new city slogan that will replace I.Seoul.U. The city government has set up a task force committee for the new slogan project and plans to unveil it no later than the year's end. The new slogan will go into use next year. According to its spokesperson, Wednesday, there has been a consensus among city government officials that the current brand I.Seoul.U is not appealing or competitive enough to draw the attention of international travelers and foreign investors, compared to those of other global cities such as New York or Amsterdam. I.Seoul.U has been the capital's slogan for years since being selected through a public contest in 2015."}
'''