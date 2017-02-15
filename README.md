# NOAA Station Data Extraction
A Python script to extract data from a weather station's CSV file.

I wanted to extract the weather information for a select few stations from the daily reports available on NOAA's website (ftp://ftp.ncdc.noaa.gov/pub/data/ghcn/daily/by_year/). Those reports contain daily data from almost all the active weather stations throughout the world for the various types of weather data that they collect.

I wrote this script to accept a CSV file from a given year, and generate a new CSV file for each station chosen. I used the simple weather data types that I wanted.

To make it easier to extract information from multiple weather stations, I edited it to generate a CSV file for each station.
