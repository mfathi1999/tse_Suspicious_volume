import csv
import os
from DatabaseManager import DBManager

colName = "symbols"
dbObject = DBManager("mongodb://mongoadmin:secret@127.0.0.1:27017/","myData","symbols")


def Average(lst):
    return sum(lst) / len(lst)

def main():

    file_directorys = os.listdir('./tickers_data')

    for path in file_directorys:
        
        file = open('./tickers_data/{}'.format(path))
        csvReader = csv.reader(file)
        
        
        
        rows=[]
        for row in csvReader:
            #print (row)
            rows.append(row)
        
        if len(rows) < 31 : #delete this symbol from list
            pass     

        else: #calcute average volumn in month


            #add Symbol to DB
            dbObject.makeSymbol(path.split('.')[0])


            month_volum_averages = []
            for row_number in range(1,len(rows)):
                month_volum_averages.append(float( rows[row_number][6]))
                if row_number > 30:
                    
                    avg = Average(month_volum_averages) #average_month of this day
                    
                    #add date if mashkok
                    if avg <= float(rows[row_number][6]):

                        dbObject.addDate(path.split('.')[0],rows[row_number][0])
                    
                    month_volum_averages.pop(0)  
                    


    




