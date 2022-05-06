import requests
import datetime
import csv
import re
import random
from bs4 import BeautifulSoup
from proxyreq import *
from input import *
from login_system import *

user_agent_list = 'Mozilla/5.0 (X11; Linux x86_64; rv:99.0) Gecko/20100101 Firefox/99.0'
db_col2 = db["data_chart"]
def enter_choice():
    while True:
        print("Select the url of the website")
        print("Press 1 for Snapdeal")
        print("Press 2 for Amazon India")
        print("Press 0 to exit")
        choice = input_integer()
        if(choice==1):
            product_url = input("Enter the url")
            headers = {"user agent":user_agent_list}
            try:
                page = requests.get(url=product_url, headers=headers)
            except requests.exceptions.HTTPError as err:
                raise SystemExit(err)
            soup = BeautifulSoup(page.content,'lxml')
            title = soup.find(class_ = 'pdp-e-i-head').get_text(strip=True)
            #print(title)
            price = soup.find(class_ = 'payBlkBig').get_text(strip=True)
            #print(price)
            print("Enter the alert price to notify you")
            alert_price = input_decimal()
            current_time = datetime.datetime.now()
            id = get_id_by_username(verify_user)
            webcode = "snapdeal"
            database_insert_data_chart(id,title,price,product_url,current_time,webcode)
        if(choice==2):
            product_url = input("Enter the url")
            headers = {"user agent":user_agent_list}
            try:
                page = requests.get(url=product_url, headers=headers)
            except requests.exceptions.HTTPError as err:
                raise SystemExit(err)
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
            id = get_id_by_username(verify_user)
            webcode = "amazon"
            database_insert_data_chart(id,title,price,product_url,current_time,webcode)
        if(choice==0):
            break
        else:
            print("Enter the right choice")




def database_insert_data_chart(id,title,price,product_url,timestamp,webcode):
    data_insert = { "userid":id,"product_name":title,"price":price,"url":product_url,"timestamp":timestamp,"webcode":webcode}
    db_col2.insert_one(data_insert)


#for i in range(1,4):
#user_agent = random.choice(user_agent_list)
#proxy = choice(get_working_proxies())
print("Welcome to the system. Please register or login")
print("Options: register | login | exit")
while True:
    option = input("> ")
    if option == "login":
        verify_user = login()
        if verify_user != 0:
            enter_choice()
        else:
            print("Login failed")
    elif option == "register":
        register()
    elif option == "exit":
        break
    else:
        print(option + " is not an option")

