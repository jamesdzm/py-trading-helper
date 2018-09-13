# Python Script focusing on price action and
# technical analysis for FX and Cryptos (or any asset)
# @author James Miles, Github: jamesdzm

import os
import requests

API_KEY = os.environ["API_KEY"]
BASE_URL = "https://www.alphavantage.co/query?" # TODO: Take URL params as separate inputs (gui, web?)
REQUEST_URL = "https://www.alphavantage.co/query?function=FX_INTRADAY&from_symbol=USD&to_symbol=JPY&interval=5min"

def get_price_data(url):
    # GET REQUEST_URL
    price_data = ""
    return price_data

def analyse_price_data(price_data):
    return None