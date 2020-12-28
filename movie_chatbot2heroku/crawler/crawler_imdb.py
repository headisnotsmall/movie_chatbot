import requests
from bs4 import BeautifulSoup as bs
import json
import os

page = 1

while page < 200:
    try:
        url = "https://www.imdb.com/search/title/?groups=top_1000&sort=user_rating,desc&count=100&start=" + str(page) + "&ref_=adv_nxt"
        p = requests.get(url).text
    #     html = p
    #     main_content = html.find_all('div', id_="lister-item-content") # movie pack
    #     for content in main_content:
    #         name = content.find_all("a")
    #         score = content.find_all("strong")
    #         print(name.text, score.text)
    #     page += 100
    except:
        pass
print(p)