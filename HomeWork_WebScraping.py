import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

response = requests.get('https://habr.com/ru/',  headers={'User-Agent': UserAgent().chrome})
response.raise_for_status()

text = response.text
soup = BeautifulSoup(text, features='html.parser')

KEYWORDS = {'дизайн', 'фото', 'web', 'Python *'}

articles = soup.find_all('article')
for article in articles:
    hubs = article.find_all('span', class_='tm-article-snippet__hubs-item')
    hubs_text = {hub.text for hub in hubs}

    for hub_text in hubs_text:
        if KEYWORDS & hubs_text:
            title = article.find('h2')
            link = title.find('a').attrs.get('href')
            url = 'https://habr.com' + link
            date = article.find('time').attrs.get('title')
            print(date)
            print(title.text)
            print(url)

