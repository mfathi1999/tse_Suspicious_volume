import pytse_client as tse
import average
from FrequentPattern import ECLAT


def download_symbols_data():
    tickers = tse.download(symbols="all", write_to_csv=True)

def calcute_Suspicious_volume():
    average.main()

def show_frequent_patterns():
    pass

def calcute_frequent_patterns(min_support):
 
    eclat = ECLAT()
    eclat.Min_support = min_support
    eclat.run_ECLAT(0)




if __name__ == "__main__":
    #download_symbols_data()
    # print("start calcute :)n")
    calcute_Suspicious_volume(100)
    print("start finding frequent pqatterns :)")