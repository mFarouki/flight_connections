from constants import flight_data_website
from utils import get_beautiful_soup

URL_STARTING_STRING = 'flights-from'
KEY_TABLE_DATA_CLASS = 'flight-routes-link'


# URL_STARTING_STRING = 'flights-from-mazar-e-sharif-mzr'

def get_connections(airports_by_country: dict):
    for country, city_codes in airports_by_country.items():
        for city_code, city_data in city_codes.items():
            city_data['connections'] = []
            city_name = city_data['city name'].lower()
            url = f"{flight_data_website}/{URL_STARTING_STRING}-{city_name}-{city_code.lower()}"
            city_soup = get_beautiful_soup(url)
            table_data = city_soup.find_all('td', class_=KEY_TABLE_DATA_CLASS)
            for connection in table_data:
                connection = connection.find('a', href=True)['href'].split('-')[-1]
                city_data['connections'].append(connection)
    return airports_by_country
