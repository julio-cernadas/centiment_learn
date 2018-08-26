#!/usr/bin/env/ python3
import requests
import re
import json
import webhoseio

from datetime import datetime
from bs4 import BeautifulSoup as soup
from pprint import pprint

from core.wrapper.stock_scraper import get_company_name

def get_names(ticker):
    company_name = get_company_name(ticker).replace(".",' ').split(' ')
    if len(company_name) >= 2:
        var1 = company_name[0].lower()
        var2 = company_name[1].lower()
        return [var1,var2,ticker]
    else:
        var1 = company_name[0].lower()
        return [var1,ticker]

def get_webhose_news(ticker):
    webhoseio.config(token="517a4e21-e484-4eac-aa8c-f50916e8db85")
    names = get_names(ticker)
    query_params = {
        "q": f"""language:english thread.country:US published:>1483232461 (site_category:stocks) ({ticker} OR {names[0]} OR {names[-1]})
                (site_type:blogs OR site_type:discussions) (thread.title:'{ticker}' OR thread.title:'{names[0]}' OR thread.title:'{names[-1]}')""",
        "ts": "1533754757303",
        "sort": "published"
        }
    output = [x for x in webhoseio.query("filterWebContent", query_params)['posts']]
    lst = [[y['published'],
            y['text'].replace('\n',' ').lower().split('. ')] for y in output]
    webhose_new = [[datetime.strptime(date.split('T')[0],'%Y-%m-%d').date(),
                    re.sub('// no comments|posted by','',text)] 
                    for date,y in lst for text in y if len(text) < 200
                    for var in names if var in text]
    return webhose_new

def get_barrons_news(ticker):
    link = f'https://www.barrons.com/search?keyword={ticker}&numResults=75&sort=date-desc&author=&searchWindow=0&minDate=&maxDate=&source=barrons'
    source = requests.get(link, proxies={'http':'50.207.31.221:80'}).text
    s = soup(source, 'lxml')    
    articles = s.find('div',{"class" : "tab-pane active"})
    lst = []
    for row in articles.findAll('li'):
        date  = ' '.join(row.find('span',{'class' : 'date'}).text.split(' ')[:3])
        date  = datetime.strptime(date,'%b %d, %Y').date()
        news  = row.find('span',{'class' : 'headline'}).text.lower()
        summary = row.find('p',{'class' : 'news__summary hidden'}).text.lower()
        lst.append([date,news + ' ' + summary])
    names = get_names(ticker)
    barrons_news = [[date,text] for date,text in lst
                                for var in names 
                                if var in text]
    return barrons_news

def get_finviz_news(ticker):
    source = requests.get(f'https://finviz.com/quote.ashx?t={ticker}', proxies={'http':'50.207.31.221:80'}).text
    s    = soup(source, 'lxml')
    articles = s.find('table',{ "class" : "fullview-news-outer" })
    x    = [row.text.split('\xa0\xa0') for row in articles.findAll('tr')]
    lst  = "CNBC|American City Business|Investor's Business|Financial|Motley|The Wall Street"
    t    = [[z,re.sub(lst,'',' '.join(y.split(' ')[:-1]).replace("\xa0",' '))] for z,y in x]
    lst  = []
    news = []
    for x,y in t:
        date = x.split(' ')
        if len(date) == 2:
            news_date = datetime.strptime(date[0],'%b-%d-%y').date()
            lst.append(news_date)
            news.append([lst[-1],y.lower()])
        elif len(date) == 1:
            news.append([lst[-1],y.lower()])
    names = get_names(ticker)
    finviz_news = [[date,text] for date,text in news
                                for var in names 
                                if var in text]
    return finviz_news

def get_ticker_news(ticker):
    news = get_barrons_news(ticker) + get_finviz_news(ticker) + get_webhose_news(ticker)
    news.sort(key=lambda r:r[0])
    return news
