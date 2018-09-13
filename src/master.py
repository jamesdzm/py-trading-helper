# Python Script focusing on price action and
# technical analysis for FX and Cryptos (or any asset)
#
# Author: James Miles, Github: jamesdzm

import os
import json
import requests
import pandas as pd

API_KEY = os.environ["API_KEY"]
BASE_URL = "https://www.alphavantage.co/query?" # TODO: Take URL params as separate inputs (gui, web?)
REQUEST_URL = "https://www.alphavantage.co/query?function=FX_INTRADAY&from_symbol=USD&to_symbol=JPY&interval=1min" + "&apikey=" + API_KEY

def get_live_price_data():
    price_data = requests.get(REQUEST_URL)
    price_data_json = json.loads(price_data.text)
    price_data_json = price_data_json["Time Series FX (1min)"]
    return price_data_json

def df_price_data(price_data):
    price_data_x = pd.DataFrame.from_dict(price_data, orient="index").reset_index()
    # Cache data as local CSV whilst testing to avoid rate limit
    price_data_x.to_csv(os.path.join(os.path.dirname(__file__), "data/csv/usd_jpy_1m.csv"), encoding="utf-8", index=False, header=True)
    print("From live:")
    print(price_data_x.head())
    return price_data_x

def get_cached_price_data():
    price_data = pd.read_csv(os.path.join(os.path.dirname(__file__), "data/csv/usd_jpy_1m.csv"))
    print("From cache:")
    print(price_data.head())
    return price_data

# data = get_live_price_data()
# data_x = df_price_data(data)
data_x = get_cached_price_data()

def analyse_price_data(price_data):
    h_height = max(price_data["2. high"])
    print("Highest high: {0}".format(h_height))

    l_low = min(price_data["3. low"])
    print("Lowest low: {0}".format(l_low))

    n_records = len(price_data["index"])
    print("Over the last {0} candles".format(n_records))
    
    peak_range = round((h_height - l_low)*100, 2)
    print("Peak range over the above period is {0} pips".format(peak_range))
    return None

analyse_price_data(data_x)