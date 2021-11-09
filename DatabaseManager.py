from typing import List
import pymongo
from pymongo.message import insert

class DBManager:
    def __init__(self, url , dbName , colName):
        self.url = url
        self.dbName = dbName
        self.col = colName
        
    def set_Collection_name(self , colName):
        self.col = colName

    def makeCollection(self):
        myclient = pymongo.MongoClient(self.url)
        mydb = myclient[self.dbName]

        try:
            mydb.create_collection(self.col)

        except:
            pass


        res = False
        if self.col in mydb.list_collection_names():
            res = True
    
        myclient.close()

        if res:
            return "collection created"
        else:
            return "collection creation faild"
    
    def insert_data(self,data):
        myclient = pymongo.MongoClient(self.url)
        mydb = myclient[self.dbName]
        mycol = mydb[self.col]

        if self.col in mydb.list_collection_names():
            mycol.insert_one(data)

            
        myclient.close()
    
    def update_item_By_Name(self , symbolName,new_data):
        myclient = pymongo.MongoClient(self.url)
        mydb = myclient[self.dbName]
        mycol = mydb[self.col]

        myquery = { "name": symbolName }
        newvalues = { "$set": new_data}

        mycol.update_one(myquery, newvalues)

    def find_item_By_Name(self, name ):

        myclient = pymongo.MongoClient(self.url)
        mydb = myclient[self.dbName]
        mycol = mydb[self.col]

        return mycol.find_one({"name": name})
        # return mycol.find_one()
        # return mycol.find({"name": {"$eq": name}})
        # return mycol.find({"name":"قولاد"})

    def find_item_By_id(self , id):
        myclient = pymongo.MongoClient(self.url)
        mydb = myclient[self.dbName]
        mycol = mydb[self.col]

        return mycol.find_one({"_id": id})

    def find_all_numberOf_SusVolume(self):
        myclient = pymongo.MongoClient(self.url)
        mydb = myclient[self.dbName]
        mycol = mydb[self.col]

        # susVolume = mycol.find({},{"_id":0,"name":0 , "dates":0 ,"numberOf_SusVolume" : 1})
        susVolume = mycol.find({},{"numberOf_SusVolume" : 1})
        

        myclient.close()
        return susVolume


    def makeSymbol(self, symbolName):
        data = {"name" : symbolName , "dates" : [] , "numberOf_SusVolume" : 0}
        self.insert_data(data)

    def addDate(self,symbolName, date):
        item = self.find_item_By_Name(symbolName)
        dates = list( item['dates'])
        dates.append(date)
        number = int (item['numberOf_SusVolume'])
        number +=1

        new_data = {"dates" : dates , "numberOf_SusVolume" : number}
        self.update_item_By_Name(symbolName , new_data)  
        
    def add_new_itemsets(self , item1 , item2 , shareDates ):
        new_dates_list = list(shareDates)
        names = []

        if type(item1["name"]) == list:
            for item_name in item1["name"]:
                if not (item_name in names):
                    names.append(item_name) 
                    # names.add(item_name)
        else:
            if not (item1["name"] in names):
                names.append(item1["name"])
                # names.add(item1["name"])


        if type(item2["name"]) == list :
            for item_name in item2["name"]:
                if not (item_name in names):
                    names.append(item_name)
                    # names.add(item_name)
        else:
            if not (item2["name"] in names):   
                names.append(item2["name"])
                # names.add(item2["name"])

        # names = list(names)
        names.sort()
        if self.find_item_By_Name(names) == None and len(names) > 0:    
            new_data = {"name" : names , "dates" : new_dates_list , "numberOf_SusVolume" : len(new_dates_list) }
            self.insert_data(new_data)
            return True
        else:
            return False

    

    def itemset_exist_by_name(self , name):

        pass

    def drop_collection_by_name(self , name):
        
        myclient = pymongo.MongoClient(self.url)
        mydb = myclient[self.dbName]


        mycol = mydb[name]
        mycol.drop()

    def drop_all_F_collections(self , F_number):
        for num in range(1 ,F_number + 1):
            self.drop_collection_by_name(f"F_{num}")


