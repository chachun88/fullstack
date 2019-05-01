import requests
from bs4 import BeautifulSoup
from .models import Category

def scrapy():
    r = requests.get("http://books.toscrape.com/index.html")
    soup = BeautifulSoup(r.text, 'html.parser')
    #categories = soup.select("div.side_categories ul ul li a")
    #for c in categories:
    #    cat = Category(name=c.get_text().strip())
    #    cat.save()
    #products_links = soup.select("article.product_pod h3 a")
    #for pl in products_links:
    #    print(pl["href"])
    #    #r = requests.get("http://books.toscrape.com/index.html")
    next = soup.select_one("ul.pager li.next > a")
    print(next["href"])
