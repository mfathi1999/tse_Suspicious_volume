#calcute and make frequent patterns


# make 1 item sets
# then 2 item sets
# then 3 item sets ...


from DatabaseManager import DBManager


class ECLAT:

    def __init__(self):
        self.Min_support = 0
        self.dbObject = DBManager("mongodb://mongoadmin:secret@127.0.0.1:27017/","myData","")

    # calcute Minimum support use Median.
    def cal_MinSupport(self): 
        self.dbObject.set_Collection_name("symbols")
        
        susVolumes_with_id  = self.dbObject.find_all_numberOf_SusVolume()
        
        susVolumes = []
        for item in susVolumes_with_id:
            susVolumes.append(item["numberOf_SusVolume"])

        
        self.Min_support = sum(susVolumes) / len(susVolumes)
        
        return self.Min_support

        

    # set Minsupport Manualy. Minsupport should be between 0 and 1 =>>  {1 >= MinSupport >= 0}
    def set_MinSupport(self, min_mount):
        self.Min_support = min_mount

    # collection format :  {1 or 2 or 3 ...}_item_sets
    # collection structure
    '''
        _id : id_Object
        names : Array[]
        dates : Array []
        numberOf_SusVolume : int
    '''
    
    
    def Intersection(self , *sets):
        common_sub_set = set( sets[0])
        for set_index in range(1,len(sets)):
            common_sub_set = set(common_sub_set).intersection(sets[set_index])
        return common_sub_set