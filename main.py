import os 
import csv
import datetime as datetime

from tvDatafeed import TvDatafeed, Interval
from Indicator import get_bbwp
from tickers import CRYPTO_LIST, CRYPTO_LIST_SHORT

if not os.path.exists('sim_results'):
    os.makedirs('sim_results')


tv = TvDatafeed()
# parameters
length = 13
bbwp_lookback = 252
interval = Interval.in_4_hour
exchange='BINANCE'
squeeze_level = 10


bbwp_squeezed = {} 
count = 0

for ticker in CRYPTO_LIST:
    count +=1 
    try:
        bbwp = get_bbwp(tv, ticker, exchange, interval, length, bbwp_lookback)
        print('{}:{}  {} out of {}'.format(ticker, bbwp, count, len(CRYPTO_LIST)))
        if bbwp < squeeze_level and bbwp > 0 :
            bbwp_squeezed[ticker] = bbwp
            print(ticker)
    except:
        tv = TvDatafeed()
        print("An exception occurred")

extension = ".csv"
file_name = os.getcwd() + "/sim_results/" + f"{datetime.datetime.now():%Y-%m-%d %H-%M-%S}" + extension
print(file_name)
print("SQUEEEEEZE")

with open(file_name, 'w') as myfile:
    wr = csv.writer(myfile)
    # wr.writerow(results)
    for key in bbwp_squeezed:
        wr.writerow(['{} : {}'.format(key, bbwp_squeezed[key])])
        print('{} : {}'.format(key, bbwp_squeezed[key]))
