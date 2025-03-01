import requests


url = "https://n.news.naver.com/article/newspaper/009/0005451788?date=20250301"
respond = requests.get(url)
print(respond.content)
