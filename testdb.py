import pymongo
import dns

myclient = pymongo.MongoClient("mongodb+srv://traxtr-admin:<password>@traxtr-cluster.nptfv.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
mydb = myclient["traxtr"]
mycol = mydb["delete2"]
#mylist = [{ "name": "Amy", "address": "Apple st 652"},{ "name": "Hannah", "address": "Mountain 21"},{ "name": "Michael", "address": "Valley 345"},{ "name": "Sandy", "address": "Ocean blvd 2"},{ "name": "Betty", "address": "Green Grass 1"}]
#x = mycol.insert_many(mylist)
username = input("name :")
mylist2 = {"name":username}
mydoc = mycol.find(mylist2)
y = []
for x in mydoc:
    y.append(x)
print(y)
if not y:
    print("empty")
else:
    print("not empty")
