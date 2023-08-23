import logging

from extract_csv import build_df, write_csv
from get_airports_by_country import get_airports_by_country
from get_connections import get_connections

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.FileHandler("run.log"), logging.StreamHandler()],
)


def log_info(message: str):
    logging.info(message)


def run():
    log_info("getting airports in each country")
    airports_by_country = get_airports_by_country()
    log_info("getting connections for each airport")
    airports_by_country = get_connections(airports_by_country)
    log_info("collating data into csvs")
    df = build_df(airports_by_country)
    write_csv(df, "connections.csv", "country_connections.csv")


if __name__ == "__main__":
    run()
