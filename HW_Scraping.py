import requests
import bs4

# добавила несколько элементов в список KEYWORDS
KEYWORDS = ['дизайн', 'фото', 'web', 'python', 'модель', 'деятельность', 'частота', 'гитхаб']
HEADERS = {'Accept': '*/*', 'Connection': 'keep-alive',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36',
           'Accept-Language': 'en-US;q=0.5,en;q=0.3', 'Cache-Control': 'max-age=0', 'Pragma': 'no-cache'}

base_url = 'https://habr.com'
url = base_url + '/ru/all/'

def get_soup(url):
    response = requests.get(url, headers=HEADERS)
    text = response.text
    soup = bs4.BeautifulSoup(text, features="html.parser")
    return soup

def get_articles_preview():
    soup = get_soup(url)
    articles = soup.find_all("article")
    for article in articles:
        hubs = article.find_all(class_="tm-article-body tm-article-snippet__lead")
        hubs = [hub.text.strip() for hub in hubs]
        for hub in hubs:
            hub = hub.split()
            for el in hub:
                el = el.lower()
                if el in KEYWORDS:
                    date = article.find(class_="tm-article-snippet__datetime-published").find("time").text
                    title = article.find("h2").find('span').text
                    href = article.find(class_="tm-article-snippet__title-link").attrs["href"]
                    link = base_url + href
                    print(f"{date} - {title} - {link}")

def get_articles_text():
    soup = get_soup(url=url)
    articles = soup.find_all("article")
    for article in articles:
        href = article.find(class_="tm-article-snippet__title-link").attrs["href"]
        url_articles = base_url + href
        soup = get_soup(url=url_articles)
        text = soup.text
        text = text.split()
        for el in text:
            if el in KEYWORDS:
                title = article.find("h2").find('span').text
                href = article.find(class_="tm-article-snippet__title-link").attrs["href"]
                link = base_url + href
                print(f'KEYWORD: "{el}". Название: {title} ==> {link}')

if __name__ == '__main__':
    get_articles_preview()
    print()
    get_articles_text()
