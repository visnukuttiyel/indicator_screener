from tvDatafeed import TvDatafeed, Interval
from Indicator import get_bbwp
from tickers import CRYPTO_LIST, CRYPTO_LIST_SHORT


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

# Print all scripts with bbwp less than squeeze level
print("SQUEEEEEZE")
for key in bbwp_squeezed:
    print('{} : {}'.format(key, bbwp_squeezed[key]))

