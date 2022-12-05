
from indicator import get_bbwp, get_bbw2
from tickers import CRYPTO_LIST, CRYPTO_LIST_SHORT, NSE_LIST
from databuilder import *
import yaml
import pandas as pd

with open('parameters.yaml') as f:
    parameters = yaml.safe_load(f)

data = DataBuilder(parameters, interval = Interval.in_daily, ticker_list = CRYPTO_LIST_SHORT).data.data


def get_bbwp_squeezed(data,  squeeze_level):
    bbwp_squeezed = {} 
    bbwp_squeezed['Number of tickers analysed'] = len(data)
    for ticker in data:
            bbwp = data[ticker]['BBWP'][0]
            if bbwp <  squeeze_level and bbwp > 0 :
                bbwp_squeezed[ticker] = bbwp

    return bbwp_squeezed

bbwp_squeezed = get_bbwp_squeezed(data, parameters['indicator']['bbwp']['squeeze_level'])    

wrtie_to_file(bbwp_squeezed)
