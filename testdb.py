import dns
import pymongo
import bson
import pprint
myclient = pymongo.MongoClient("mongodb+srv://traxtr-admin:<password>@traxtr-cluster.nptfv.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
mydb = myclient["traxtr"]
mycol = mydb["data_chart"]
#mylist = [{ "name": "Amy", "address": "Apple st 652"},{ "name": "Hannah", "address": "Mountain 21"},{ "name": "Michael", "address": "Valley 345"},{ "name": "Sandy", "address": "Ocean blvd 2"},{ "name": "Betty", "address": "Green Grass 1"}]
#x = mycol.insert_many(mylist)
##mylist2 = {"name":username}
#x = [ doc["name"] for doc in mycol.find({"name":"Amy"})]
#print(x)
#x =[]
#for doc in  mycol.find():
#    x.append(doc["name"])
for doc in mycol.find(): 
    print(doc)
