# Lesson 3.11 - Read more stocks
import pandas as pd

def test_run():
    start_date = '2010-01-22'
    end_date = '2010-01-26'
    dates = pd.date_range(start_date, end_date)
    df1 = pd.DataFrame(index=dates)

    dfSPY = pd.read_csv("C:/Code/Python/Udacity/data/SPY.csv",
        index_col='Date',parse_dates=True,
        usecols=['Date', 'Adj Close'], na_values=['nan'])
    dfSPY = dfSPY.rename(columns={'Adj Close':'SPY'})
    
    df1 = df1.join(dfSPY,how='inner')
    
    symbols = ['GOOG', 'IBM', 'GLD']

    for symbol in symbols:
        df_temp = pd.read_csv("C:/Code/Python/Udacity/data/{}.csv".format(symbol),
        index_col='Date',parse_dates=True,
        usecols=['Date', 'Adj Close'], na_values=['nan'])
        df_temp = df_temp.rename(columns={'Adj Close': symbol})
        df1 = df1.join(df_temp,how='left')
    print(df1)

if __name__ == "__main__":
    test_run()