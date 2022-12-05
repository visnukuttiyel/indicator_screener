from tqdm import tqdm
from threading import Thread
import time
import pandas as pd


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
        self.df = pd.DataFrame()
        self.read_data_thread()


    def fetch_data(self, ticker):
        # try:
        data =  pd.DataFrame(self.tv.get_hist(symbol=ticker, exchange= self.exchange, interval=self.interval, n_bars=self.lookback))
        data.set_index('symbol')

        if self.df.empty:
            self.df = data
        else:
           self.df = pd.concat([self.df, data])
        # except:
        #      self.df[ticker] = {}
        #      self.tv = TvDatafeed()
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

    def reset_index(self):
        self.df = self.df.reset_index(inplace=True)  
        self.df =self.df.set_index('symbol')
