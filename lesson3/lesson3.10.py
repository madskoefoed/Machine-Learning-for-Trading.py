# Lesson 3.10 - Types of "join"
import pandas as pd

def test_run():
    start_date = '2010-01-22'
    end_date = '2010-01-26'
    dates = pd.date_range(start_date, end_date)
    df1 = pd.DataFrame(index=dates)

    dfSPY = pd.read_csv("C:/Code/Python/Udacity/data/SPY.csv",
        index_col='Date',parse_dates=True,
        usecols=['Date', 'Adj Close'], na_values=['nan'])
    
    df1 = df1.join(dfSPY,how='inner')
    print(df1)

if __name__ == "__main__":
    test_run()