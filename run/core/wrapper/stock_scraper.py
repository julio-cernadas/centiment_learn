#!/usr/bin/env/ python3
import json
import requests
import pandas as pd
from datetime import date, timedelta

def get_prices_df(ticker):
    url = "https://www.alphavantage.co/query"
    function = "TIME_SERIES_DAILY_ADJUSTED"
    symbol = ticker
    outputsize= "compact"
    api_key = "4I16NYFU17Q3KNKC"
    data = { "function": function,
            "symbol": symbol,
            "outputsize": outputsize,
            "apikey": api_key }
    try:
        dictionary = requests.get(url, params = data).json() 
        keys = list(dictionary.keys())
        series = keys[1]
        resp = dictionary[series]
        df = pd.DataFrame.from_dict(resp, orient='index')
        df['date'] = pd.to_datetime(df.index)
        fivemonthsago = date.today() - timedelta(140)
        df = df.rename(columns={"5. adjusted close": "Price"})
        df = df[(df['date']>=fivemonthsago)][['Price','date']].set_index('date')
        return df
    except:
        return None

def get_company_name(ticker):
	try:
		endpoint = 'http://dev.markitondemand.com/MODApis/Api/v2/Quote/json?symbol='+ticker
		response = requests.get(endpoint).json()
		company_name = response['Name']
		return company_name
	except:
		return 'N/A'

def get_info_from_request(search):
	endpoint = 'http://dev.markitondemand.com/MODApis/Api/v2/Lookup/json?input='+search
	response = requests.get(endpoint).json()[0]
	try:
		ticker = response['Symbol']
		company_name = response['Name']
		exchange = response['Exchange']
		return ticker,company_name,exchange
	except:
		return 'N/A','N/A','N/A'

def get_info_from_result(ticker):
	endpoint   = 'http://dev.markitondemand.com/MODApis/Api/v2/Quote/json?symbol='+ticker
	try:
		response   = requests.get(endpoint).json()
		last_price = response['LastPrice']
		change     = response['ChangePercent']
		market_cap = response['MarketCap']
		volume     = response['Volume']
		ytd        = response['ChangeYTD']
		ytd_percnt = response['ChangePercentYTD']
		return last_price,change,market_cap,volume,ytd,ytd_percnt
	except:
		return 'N/A','N/A','N/A','N/A','N/A','N/A'
