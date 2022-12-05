from datareader import *

class DataBuilder():
    def __init__(self, parameters, interval = Interval.in_daily, ticker_list = CRYPTO_LIST_SHORT):
        self.parameters = parameters
        self.df = DataReader(interval = interval, lookback = parameters['ticker']['lookback'], ticker_list = ticker_list).df
        self.build_indicators()

    def build_indicators(self):
        self.bbwp()

    def bbwp(self):
        for ticker in self.df:
            self.data.data[ticker][self.parameters['indicator']['bbwp']['name']] = get_bbw2(self.data.data[ticker]['close'], self.parameters['indicator']['bbwp']['length'])
 