import pymongo

client = pymongo.MongoClient("mongodb+srv://traxtr-admin:<password>@traxtr-cluster.nptfv.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client["traxtr"]
db_col = db["data_chart"]
def get_userid_by_url(url):
    return (db_col.find_one({"url":url})["userid"])

def get_title_by_url(url):
    return (db_col.find_one({"url":url})["product_name"])

def get_price_by_url(url):
    return (db_col.find_one({"url":url})["price"])

def get_webcode__by_url(url):
    return (db_col.find_one({"url":url})["webcode"])

