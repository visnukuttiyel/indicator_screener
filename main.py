
from indicator import get_bbwp, get_bbw2
from tickers import CRYPTO_LIST, CRYPTO_LIST_SHORT, NSE_LIST
from datareader import *

data_reader = DataReader(ticker_list = CRYPTO_LIST_SHORT)

# parameters
length = 13
squeeze_level = 10


def get_bbwp_squeezed(data_reader, length, squeeze_level):
    bbwp_squeezed = {} 
    bbwp_squeezed['Number of tickers analysed'] = len(data_reader.data)
    for ticker in data_reader.data:
        try:
            bbwp = get_bbw2(data_reader.data[ticker]['close'], length)
            if bbwp < squeeze_level and bbwp > 0 :
                bbwp_squeezed[ticker] = bbwp
        except:
            pass
    return bbwp_squeezed

bbwp_squeezed = get_bbwp_squeezed(data_reader, length, squeeze_level)    

wrtie_to_file(bbwp_squeezed)
