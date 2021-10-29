import pymongo
from DatabaseManager import DBManager


dbObject = DBManager("mongodb://mongoadmin:secret@127.0.0.1:27017/","myData","symbols")

# dbObject.makeCollection()
# dbObject.makeSymbol("کیمیاتک")
# dbObject.makeSymbol("قولاد")
# dbObject.makeSymbol("فملی")


item = dbObject.find_item_By_Name("قولاد")
print(item)

added_date = "2014-08-16"
dbObject.addDate("قولاد", added_date)

item = dbObject.find_item_By_Name("قولاد")
print(item)

# item2 = dbObject.find_item_By_id(item["_id"])
# print(item2)
# date = '2020-04-07'
# dbObject.addDate("قولاد",date)
# item = dbObject.find_item_By_Name("قولاد")



# for x in item:
#     print(x)









# myclient = pymongo.MongoClient("mongodb://mongoadmin:secret@127.0.0.1:27017/")

# mydb = myclient["myData"]
# mydb = myclient.get_database("myData")
# mycol = mydb["کیمیاتک"]


# if "myData" in myclient.list_database_names():
#     print ("db created successfully")


# print(mycol)

# mydb = myclient["myData"]
# mycol = mydb.create_collection("customers")

# mycol = mydb["customers"]


# print(mydb)
# print(mycol)

# data = { "name": "John", "address": "Highway 37" }
# print (type(data))