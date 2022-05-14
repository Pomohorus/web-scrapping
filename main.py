import requests
import bs4

url = 'https://habr.com/'

HEADERS = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Connection': 'keep-alive',
    'Cookie': '_ga=GA1.2.1670578745.1641869109; _ym_d=1641869110; _ym_uid=1609062530675671827; __gads=ID=0eee4e7354623b0e:T=1641869106:S=ALNI_MadETIh0jjf3m44O_8CocvEoJstTw; fl=ru; hl=ru; cto_bundle=-tww_183MUVtRGs1aktEeW84Vkdka1JXQzRtV0JuV0xvQ1I3RTNRSlpNVGoyOVQ5QnpOT0g5NGtCb09QTFBUdEx1cURaUSUyRkJlVTZUcUFNYVlGR1lnMDBrd21zYTFlMk4lMkJDbFZIOXE3YTcwM3JQRHhqbUgzYUJCaUdtVUJkeGxIWXRnOWR2SVE4YUhLb0JlUW4xVDdMVndzYllRJTNEJTNE; habr_web_home_feed=/all/; _ym_isad=2; _gid=GA1.2.1975664003.1652534990; _gat_gtag_UA_726094_1=1',
    'Host': 'habr.com',
    'Referer': 'https://habr.com/ru/all/',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'Sec-Fetch-Dest': 'script',
    'Sec-Fetch-Mode': 'no-cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36'
}
KEYWORDS = ['CSS *', 'Python *', 'Программирование *', 'Веб-дизайн *']

responce = requests.get(url, headers=HEADERS)
responce.raise_for_status()
text = responce.text

soup = bs4.BeautifulSoup(text, features='html.parser')
articles = soup.find_all('article')
for article in articles:
    hubs = article.find_all(class_='tm-article-snippet__hubs-item')
    hubs = set(hub.text.strip() for hub in hubs)
    # print(hubs)
    for hub in hubs:
        if hub in KEYWORDS:
            href = article.find(class_='tm-article-snippet__title-link').attrs['href']
            title = article.find('h2').find('span').text
            time = article.find(class_='tm-article-snippet__datetime-published').find('time').text
            result = f'Время публикации: {time},\nНазвание статьи: {title},\nСсылка на статью: {url + href}\n\n\n'
            print(result)