import pymongo
import dns
import datetime
from bs4 import BeautifulSoup
import re
import decimal
from test_mongo_data import *
from test_email_alert import *
from test_main import *

def test_get_url_snapdeal():
    url_data_snapdeal = []
    for doc in db_col2.distinct("url",{"webcode":"snapdeal"}):
        url_data_snapdeal.append(doc)
    return url_data_snapdeal

def test_get_url_amazon():
    url_data_amazon = []
    for doc in db_col2.distinct("url",{"webcode":"amazon"}):
        url_data_amazon.append(doc)
    return url_data_amazon

def test_tracking():
    url_amazon = test_get_url_amazon()
    url_snapdeal = test_get_url_snapdeal()
    user_agent = 'Mozilla/5.0 (X11; Linux x86_64; rv:99.0) Gecko/20100101 Firefox/99.0'
    header = {"user agent": user_agent}
    for list_url in url_amazon:
        page = requests.get(url=list_url,headers = header)
        soup = BeautifulSoup(page.content,'lxml')
        try:
            price = soup.find('span',class_ = 'a-offscreen').get_text(strip=True)
            price = re.sub('[₹,]','',price)
            title = soup.find('span',class_ = 'a-size-largeproduct-title-word-break').get_text(strip=True)
        except:
            continue
        if(decimal.Decimal(price)<=decimal.Decimal(test_get_alert_price_by_url(list_url))):
            alert_me(test_get_email_id_by_userid(test_get_userid_by_url(list_url)),list_url)
        email_alert_price = test_get_alert_price_by_url(list_url)
        current_time = datetime.datetime.now()
        id = test_get_userid_by_url(list_url)
        webcode = "amazon"
        test_database_insert_data_chart(id,title,price,list_url,current_time,webcode,alert_price)
    for list_url in url_snapdeal:
        page = requests.get(url=list_url,headers = header)
        soup = BeautifulSoup(page.content,'lxml')
        title = soup.find(class_= "pdp-e-i-head").get_text(strip=True)
        price = soup.find(class_= "payBlkBig").get_text(strip=True)
        if(decimal.Decimal(price)<=decimal.Decimal(test_get_alert_price_by_url(list_url))):
            test_alert_me(test_get_email_id_by_userid(test_get_userid_by_url(list_url)),list_url)
        alert_price = test_get_alert_price_by_url(list_url)
        current_time = datetime.datetime.now()
        id = test_get_userid_by_url(list_url)
        webcode = "snapdeal"
        test_database_insert_data_chart(id,title,price,list_url,current_time,webcode,alert_price)

test_tracking()
