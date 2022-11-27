import numpy as np

def get_bbwp(tv, ticker, exchange_name, time_interval, length, bbwp_lookback):
    price_data = tv.get_hist(symbol=ticker, exchange=exchange_name, interval=time_interval, n_bars=bbwp_lookback)

    price_tp = (price_data['close']) # + price_data['open'] + price_data['high'])/3
    price_std = price_tp.rolling(length).std(ddof=0)
    price_mean = price_tp.rolling(length).mean()

    bb_upper = price_mean + 2* price_std
    bb_lower = price_mean - 2* price_std

    bbw = (bb_upper -bb_lower)/price_mean
    bbwp = 0
    for value in bbw:
        if value < bbw[-1]:
            bbwp+= 1

    bbwp = bbwp/np.count_nonzero(~np.isnan(bbw))*100
    return bbwp

def get_bbw2(price_close, length):

    price_std = price_close.rolling(length).std(ddof=0)
    price_mean = price_close.rolling(length).mean()

    bb_upper = price_mean + 2* price_std
    bb_lower = price_mean - 2* price_std

    bbw = (bb_upper -bb_lower)/price_mean
    bbwp = 0
    for value in bbw:
        if value < bbw[-1]:
            bbwp+= 1

    bbwp = bbwp/np.count_nonzero(~np.isnan(bbw))*100
    return bbwp