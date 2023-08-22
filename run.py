from get_airports_by_country import get_airports_by_country
from get_connections import get_connections


def run():
    airports_by_country = get_airports_by_country()
    airports_by_country = get_connections(airports_by_country)
    print(airports_by_country)


if __name__ == "__main__":
    run()
