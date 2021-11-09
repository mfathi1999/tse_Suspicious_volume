from typing import Pattern
import pymongo
from DatabaseManager import DBManager
from FrequentPattern import ECLAT



dbObject = DBManager("mongodb://mongoadmin:secret@127.0.0.1:27017/","myData","")
dbObject.drop_all_F_collections(18)



# dbObject.col = "F_3"

# arr = ["غدیر","آگاس"]
# print(dbObject.find_item_By_Name(arr))

eclat = ECLAT()

eclat.Min_support = 30
#eclat.cal_MinSupport()
# print(eclat.Min_support)

eclat.run_ECLAT(0)





# eclat.intersection_set()




# eclat.set_MinSupport(100)

# set1 = [1,2,3,4]
# set2 =  [3,4,5,6]
# set3 =  [3,4,7]



# print(eclat.Intersection(set1,set2,set3))
# print (set(set1).intersection(set2,set3))

# for i in range(3):
#     for j in ['a','b','c','d','e','f']:
#         print(i," ",j)
#         if j == 'c':
#             break







# pattern = F_Pattern()
# min_support = pattern.cal_MinSupport()

# # for x in min_support:
# #     # print(x["numberOf_SusVolume"])
# #     print (x)

# print (min_support)




# dbObject = DBManager("mongodb://mongoadmin:secret@127.0.0.1:27017/","myData","symbols")

# dbObject.makeCollection()
# dbObject.makeSymbol("کیمیاتک")
# dbObject.makeSymbol("قولاد")
# dbObject.makeSymbol("فملی")


# item = dbObject.find_item_By_Name("قولاد")
# print(item)

# added_date = "2014-08-16"
# dbObject.addDate("قولاد", added_date)

# item = dbObject.find_item_By_Name("قولاد")
# print(item)

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