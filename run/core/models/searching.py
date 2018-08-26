#!/usr/bin/env python3

from core.wrapper.stock_scraper import get_info_from_request, get_info_from_result

def search_api(search):
    ticker,company_name,exchange = get_info_from_request(search)
    last_price,change,market_cap,volume,ytd,ytd_percnt = get_info_from_result(ticker)
    x = [last_price,change,ytd,ytd_percnt,market_cap,volume]
    try:
        y = [round(_,2) for _ in x]
    except:
        y = x
    lst = [[ticker,company_name,exchange] + y]
    return lst,ticker