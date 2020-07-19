#!/usr/bin/env/ python3

# A script that will scrape marketbeat.com for stocks with new 52 week highs

from bs4 import BeautifulSoup
import requests

source = requests.get('https://www.marketbeat.com/market-data/52-week-highs/')

data = BeautifulSoup(source.text, 'html.parser')

tickers = data.fina_all('div', class_='ticker-area')

for i in tickers:
  print(i.text)
