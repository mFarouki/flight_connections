import pandas as pd

from constants import CITY_NAME, CONNECTIONS

COUNTRY = 'country'
AIRPORT_CODE = 'airport code'
CONNECTION = 'connection'
CONNECTION_COUNTRY = f'{CONNECTION} {COUNTRY}'


def build_df(airports_by_country: dict) -> pd.DataFrame:
    list_of_connections = []
    for country, airports in airports_by_country.items():
        for airport, airport_info in airports.items():
            for connection in airport_info[CONNECTIONS]:
                list_of_connections.append(
                    {
                        COUNTRY: country,
                        CITY_NAME: airport_info[CITY_NAME],
                        AIRPORT_CODE: airport,
                        CONNECTION: connection,
                    }
                )
    df = pd.DataFrame(list_of_connections)
    code_countries = (
        df.groupby(AIRPORT_CODE).first()[[CITY_NAME, COUNTRY]].reset_index()
    )
    df_with_connection_country = pd.merge(
        df,
        code_countries,
        left_on=CONNECTION,
        right_on=AIRPORT_CODE,
        suffixes=('', f'_{CONNECTION}'),
        how='left',
    )
    df_with_connection_country = df_with_connection_country.drop(
        columns=f'{AIRPORT_CODE}_{CONNECTION}'
    )
    df_with_connection_country = df_with_connection_country.rename(
        columns={
            f'{CITY_NAME}_{CONNECTION}': f'{CONNECTION} {CITY_NAME}',
            f'{COUNTRY}_{CONNECTION}': CONNECTION_COUNTRY,
        }
    )
    return df_with_connection_country


def write_csv(df: pd.DataFrame, full_outfile: str, country_outfile: str):
    df.to_csv(full_outfile, index=False)
    df[[COUNTRY, CONNECTION_COUNTRY]].drop_duplicates().to_csv(
        country_outfile, index=False
    )
