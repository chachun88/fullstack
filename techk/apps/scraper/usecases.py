import requests
import re
from urllib.parse import urljoin
from bs4 import BeautifulSoup
from .models import Category, Book, ExtraInformation

SCRAPY_URL = "http://books.toscrape.com/"
CATEGORIES_TAG = "div.side_categories ul ul li a"
PRODUCTS_TAG = "article.product_pod div.image_container"
PRODUCT_NAME = "div.product_main h1"
PRODUCT_PRICE = "div.product_main p.price_color"
PRODUCT_DESCRIPTION_SECTION = "div#product_description"
PRODUCT_EXTRA_INFORMATION = "table tr"

def scrapy():
    r = requests.get(SCRAPY_URL)
    soup = BeautifulSoup(r.text, 'html.parser')
    get_categories(soup)

def get_categories(soup):
    categories = soup.select(CATEGORIES_TAG)
    for c in categories:
        # TODO save cat
        get_book_list(c["href"])
    return categories

def get_book_list(url):
    url = urljoin(SCRAPY_URL, url)
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    products_links = soup.select(PRODUCTS_TAG)
    for pl in products_links:
        product_link = urljoin(url, pl.a["href"])
        thumbnail_link = urljoin(url, pl.img["src"])
        get_book(product_link, thumbnail_link)

def get_book(url, thumbnail_link):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    name = soup.select_one(PRODUCT_NAME).get_text()
    price = soup.select_one(PRODUCT_PRICE).get_text()[2:]
    description = soup.select_one(PRODUCT_DESCRIPTION_SECTION).find_next("p").get_text()

    # get extra information for book
    filas = soup.select(PRODUCT_EXTRA_INFORMATION)
    extra_information = mapper(filas)

    # TODO save book and extra information

def mapper(filas):
    extra_information = {}
    for f in filas:
        extra_name = f.th.get_text().lower()
        extra_value = f.td.get_text()

        if "upc" in extra_name:
            extra_information["upc"] = extra_value
            continue
        if "type" in extra_name:
            extra_information["product_type"] = extra_value
            continue
        if "price" in extra_name:
            extra_information["price"] = float(extra_value.strip()[2:])
            extra_information["price_with_tax"] = float(extra_value.strip()[2:])
            continue
        if "tax" in extra_name:
            extra_information["tax"] = float(extra_value.strip()[2:])
            continue
        if "availability" in extra_name:
            availability = re.findall(r'\d+', extra_value)[0]
            extra_information["availability"] = int(availability)
            continue
        if "reviews" in extra_name:
            reviews = re.findall(r'\d+', extra_value)[0]
            extra_information["reviews"] = int(reviews)
            continue

    return extra_information
