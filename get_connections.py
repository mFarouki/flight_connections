import re

from constants import CITY_NAME, CONNECTIONS, FLIGHT_DATA_WEBSITE
from utils import get_beautiful_soup

URL_STARTING_STRING = "flights-from"
KEY_TABLE_DATA_CLASS = "flight-routes-link"


def get_connections(airports_by_country: dict) -> dict:
    for country, city_codes in airports_by_country.items():
        for city_code, city_data in city_codes.items():
            city_data[CONNECTIONS] = []
            city_name = city_data[CITY_NAME].lower().replace(' ', '-')
            city_name = re.sub(r'[\(\)\.\,\']', '', city_name)
            url = f'{FLIGHT_DATA_WEBSITE}/{URL_STARTING_STRING}-{city_name}-{city_code.lower()}'
            city_soup = get_beautiful_soup(url)
            table_data = city_soup.find_all('td', class_=KEY_TABLE_DATA_CLASS)
            for connection in table_data:
                connection = connection.find('a', href=True)['href'].split('-')[-1]
                city_data[CONNECTIONS].append(connection)
    return airports_by_country
