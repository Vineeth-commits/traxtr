import requests
import datetime
import csv
import random
from bs4 import BeautifulSoup
from proxyreq import *
import re

user_agent_list = [
'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0',
]
for i in range(1,4):
    user_agent = random.choice(user_agent_list)
#proxy = choice(get_working_proxies())
product_url = input("Enter the url")
headers = {"user agent":user_agent}
page = requests.get(url=product_url, headers=headers)
soup = BeautifulSoup(page.content,'lxml')
#print(soup.prettify())
price = soup.find('span',class_ = 'a-offscreen').get_text(strip=True)
#price = re.sub('[₹,]','',price)
title = soup.find('span',class_ = 'a-size-large product-title-word-break').get_text(strip=True)
print(title)
print(price)

