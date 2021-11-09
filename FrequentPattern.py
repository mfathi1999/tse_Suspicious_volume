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
    
    
    def intersection_set(self , *sets):
        try:
            common_sub_set = set( sets[0])
            for set_index in range(1,len(sets)):
                common_sub_set = set(common_sub_set).intersection(sets[set_index])
            return common_sub_set
        except IndexError:
            return {}

    def run_ECLAT(self,step):
        
        # fetch all itemset from database
        if step == 0:
            self.dbObject.col = "symbols"
        else:
            self.dbObject.col = f"F_{step}"
        
        current_itemsets = self.dbObject.find_all_numberOf_SusVolume()



        # find itemsets that {numberOf_SusVolume} equal or graiter than Min_support
        next_itemsets = []
        for x in current_itemsets:
            if int(x['numberOf_SusVolume']) >= self.Min_support:
                next_itemsets.append( self.dbObject.find_item_By_id(x['_id']))

        # put finded itemset to next document
        have_new_itemset_flag = False
        if len(next_itemsets) > 0 :
            self.dbObject.col = f"F_{step+1}"
            self.dbObject.makeCollection()

            for item in next_itemsets:
                self.dbObject.insert_data(item)

            # find Intersection between all itemsets
            for first_item_index in range(len(next_itemsets)):
                shares ={}
                for second_item_index in range(first_item_index+1 , len(next_itemsets) ):
                    shares = self.intersection_set(next_itemsets[first_item_index]['dates'] , next_itemsets[second_item_index]['dates'])
                    # add new itemset
                    if len(shares) >= self.Min_support:
                        have_new_itemset_flag = self.dbObject.add_new_itemsets(next_itemsets[first_item_index],next_itemsets[second_item_index], shares)
        
        # there is new itemsets
        if have_new_itemset_flag:
            self.run_ECLAT(step+1)
