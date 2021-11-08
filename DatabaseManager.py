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
        


    



