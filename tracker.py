import pymongo
import dns
import datetime
from bs4 import BeautifulSoup
import re
from mongo_data.py import *

def get_url_snapdeal():
    url_data_snapdeal = []
    for doc in db_col.distinct("url",{"webcode":"snapdeal"}):
        url_data_snapdeal.append(doc)
    return url_data_snapdeal

def get_url_amazon():
    url_data_amazon = []
    for doc in db_col.distinct("url",{"webcode":"amazon"}):
        url_data_amazon.append(doc)
    return url_data_amazon

def tracking():
    url_amazon = get_url_amazon()
    url_snapdeal = get_url_snapdeal()
    user_agent = 'Mozilla/5.0 (X11; Linux x86_64; rv:99.0) Gecko/20100101 Firefox/99.0'
    header = {"user agent": user_agent}
    for list_url in url_amazon:
        page = requests.get(url=list_url,headers = headers)
        soup = BeautifulSoup(page.content,'lxml')
        price = soup.find('span',class_ = 'a-offscreen').get_text(strip=True)
        price = re.sub('[₹,]','',price)
        title = soup.find('span',class_ = 'a-size-largeproduct-title-word-break').get_text(strip=True)
                
        
