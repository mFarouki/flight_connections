# Flight Connections

Finds which cities and countries have flight connections (currently only considers direct connections). Pulls data from
flightconnections.com and writes out two csv files:

- [connections.csv](output/connections.csv): this shows city-by-city connections
- [country_connections.csv](output/country_connections.csv): this is a simplified view, showing only which countries
  have direct connecting flights to each other

As this repo scrapes data from the website, it can only function so long as the site html takes the same format. If this
changes, the code will of course need tweaking.