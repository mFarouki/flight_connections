import requests
from bs4 import BeautifulSoup


def get_beautiful_soup(url: str):
    country_page = requests.get(url)
    return BeautifulSoup(country_page.content, "html.parser")
