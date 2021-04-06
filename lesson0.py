import os
import pandas as pd
import pandas_datareader.data as web
from datetime import date

symbols = ['AAPL', 'AMAT', 'ATX', 'CARA', 'GLD', 'GOLD','GOOG', 'IBM', 'SPY', 'XOM']

def get_stock_csv(symbol, start_date, end_date, filename):
    dframe = web.DataReader(name=symbol, data_source='yahoo', start=start_date, end=end_date)
    dframe.to_csv(filename)
    return dframe

for symbol in symbols:
    get_stock_csv(symbol, "1990-01-01", date.today(), "C:/Code/Python/Udacity/data2/{}.csv".format(symbol))