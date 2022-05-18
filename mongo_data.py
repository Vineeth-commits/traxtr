import pymongo

client = pymongo.MongoClient("mongodb+srv://traxtr-admin:traxtr-passkey123@traxtr-cluster.nptfv.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client["traxtr"]
db_col = db["data_chart"]
db_col_login = db["login_system"]
def get_userid_by_url(url):
    return (db_col.find_one({"url":url})["userid"])

def get_title_by_url(url):
    return (db_col.find_one({"url":url})["product_name"])

def get_price_by_url(url):
    return (db_col.find_one({"url":url})["price"])

def get_webcode__by_url(url):
    return (db_col.find_one({"url":url})["webcode"])

def get_alert_price_by_url(url):
    return (db_col.find_one({"url":url})["alert_price"])

def get_email_id_by_userid(userid):
    return (db_col_login.find_one({"_id":userid})["email"])

