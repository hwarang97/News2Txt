import requests
from bs4 import BeautifulSoup

url = "https://n.news.naver.com/article/newspaper/009/0005451788?date=20250301"
respond = requests.get(url).text

soup = BeautifulSoup(respond, "html.parser")
title = soup.find(name="h2", id="title_area").getText()
contents = soup.find(name="article").getText().replace('\n',' ')

with open("article.txt", mode="w") as file:
    file.write(contents)
