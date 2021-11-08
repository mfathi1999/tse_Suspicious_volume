import pytse_client as tse
import average

def download_symbols_data():
    tickers = tse.download(symbols="all", write_to_csv=True)

def calcute_Suspicious_volume():
    average.main()

def show_frequent_patterns():
    pass

def calcute_frequent_patterns():
    pass


if __name__ == "__main__":
    #download_symbols_data()
    print("start calcute :)n")
    calcute_Suspicious_volume()