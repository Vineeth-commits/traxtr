import requests
import datetime
import csv
import re
import random
from bs4 import BeautifulSoup
from proxyreq import *
from input import *

user_agent_list = [
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11',
    'Opera/9.25 (Windows NT 5.1; U; en)',
    'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
    'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.12) Gecko/20070731 Ubuntu/dapper-security Firefox/1.5.0.12',
    'Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/1.2.9'
]
for i in range(1,4):
    user_agent = random.choice(user_agent_list)
#proxy = choice(get_working_proxies())
while True:
    print("Select the url of the website")
    print("Press 1 for Snapdeal")
    print("Press 2 for Amazon India")
    print("Press 0 to exit")
    choice = input_integer()
    if(choice==1):
        product_url = input("Enter the url")
        headers = {"user agent":user_agent}
        page = requests.get(url=product_url, headers=headers)
        soup = BeautifulSoup(page.content,'lxml')
        #print(soup.prettify())
        title = soup.find(class_ = 'pdp-e-i-head').get_text(strip=True)
        print(title)
        price = soup.find(class_ = 'payBlkBig').get_text(strip=True)
        print(price)
        print("Enter the alert price to notify you")
        alert_price = input_decimal()
        current_time = datetime.datetime.now()
    if(choice==2):
        product_url = input("Enter the url")
        headers = {"user agent":user_agent}
        page = requests.get(url=product_url, headers=headers)
        soup = BeautifulSoup(page.content,'lxml')
        #print(soup.prettify())
        price = soup.find('span',class_ = 'a-offscreen').get_text(strip=True)
        price = re.sub('[₹,]','',price) 
        print(price)
        title = soup.find('span',class_ = 'a-size-large product-title-word-break').get_text(strip=True)
        print(title)
        print("Enter the alert price to notify you")
        alert_price = input_decimal()
        current_time = datetime.datetime.now()
    if(choice==0):
        break
    else:
        print("Enter the right choice")
#filename = "data_chart.csv"
#fields = ['title','price','timeStamp', 'link']
#rows = [title,price, current_time,product_url]
#with open(filename, 'a') as csvfile:
#    csvwrite = csv.writer(csvfile)
    #csvwrite.writerow(fields)
#    csvwrite.writerow(rows)

