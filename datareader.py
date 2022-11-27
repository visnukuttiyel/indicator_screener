from tqdm import tqdm
from threading import Thread
import time


from tvDatafeed import TvDatafeed, Interval
from indicator import get_bbwp, get_bbw2
from filewriter import wrtie_to_file
from tickers import CRYPTO_LIST, CRYPTO_LIST_HALF, NSE_LIST, NSE_MIDCAPS, CRYPTO_LIST_SHORT

# Downloads data from trading view
class DataReader():
    def __init__(self, interval = Interval.in_daily, lookback = 252, ticker_list = CRYPTO_LIST_SHORT):
        self.exchange = 'NSE' if 'NSE' in ticker_list else 'BINANCE'
        self.interval = interval
        self.lookback = lookback
        self.ticker_list = ticker_list
        self.tv = TvDatafeed()
        self.data = {}
        self.read_data_thread()

    def fetch_data(self, ticker):
        try:
            self.data[ticker] = self.tv.get_hist(symbol=ticker, exchange= self.exchange, interval=self.interval, n_bars=self.lookback)
        except:
             self.data[ticker] = {}
             self.tv = TvDatafeed()
        return True
   
    def read_data(self):
        for ticker in tqdm(self.ticker_list):
            self.fetch_data(ticker)

    def read_data_thread(self):
        threads = []
        for ticker in tqdm(self.ticker_list):
                process = Thread(target=self.fetch_data, args=[ticker])
                process.start()
                time.sleep(.5) # sleep in between calls to prevent crashing of tvfeed
                threads.append(process)
        for process in tqdm(threads):
            process.join(10)