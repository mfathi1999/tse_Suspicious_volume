import pytse_client as tse
import average

def download_symbols_data():
    tickers = tse.download(symbols="all", write_to_csv=True)

def calcute_Suspicious_volume():
    average.main()


if __name__ == "__main__":
    download_symbols_data()
    calcute_Suspicious_volume()