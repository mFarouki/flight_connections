from constants import AIRPORTS_BY_COUNTRY_URL, FLIGHT_DATA_WEBSITE
from utils import get_beautiful_soup

KEY_PHRASE_ALL_COUNTRIES = 'Airports in '
KEY_PARAGRAPH_CLASS = ['airport-city"']
CITY_NAME = 'city name'


def get_country_links() -> dict:
    airports_by_country_soup = get_beautiful_soup(AIRPORTS_BY_COUNTRY_URL)
    links = airports_by_country_soup.select('a')
    country_links = {}
    for link in links:
        title = link.get('title')
        if title and title.startswith(KEY_PHRASE_ALL_COUNTRIES):
            country = title.replace(KEY_PHRASE_ALL_COUNTRIES, '')
            country_links[country] = link.get('href')
    return country_links


def get_airport_codes_by_country(country_links: dict):
    airport_codes = {}
    for country, link in country_links.items():
        country_page_soup = get_beautiful_soup(f'{FLIGHT_DATA_WEBSITE}{link}')
        paragraphs = country_page_soup.select('p')
        for paragraph in paragraphs:
            paragraph_class = paragraph.get('class')
            if paragraph_class == KEY_PARAGRAPH_CLASS:
                paragraph_text = paragraph.get_text().split(' ')
                city, code = paragraph_text[0], paragraph_text[1].lower()
                if country not in airport_codes:
                    airport_codes[country] = {}
                airport_codes[country][code] = {}
                airport_codes[country][code][CITY_NAME] = city
    return airport_codes


def get_airports_by_country():
    country_links = get_country_links()
    return get_airport_codes_by_country(country_links)
