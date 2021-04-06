# Lesson 3.12 - Utility functions for reading data
import os
import pandas as pd

# Return CSV file path given ticker symbol
def symbol_to_path(symbol, base_dir='C:/Code/Python/Udacity/data'):
    return os.path.join(base_dir, '{}.csv'.format(symbol))

def get_data(symbols, dates):
    df = pd.DataFrame(index=dates)
    if 'SPY' not in symbols:
        symbols.insert(0, 'SPY')

    for symbol in symbols:
        df_temp = pd.read_csv(symbol_to_path(symbol),
            index_col='Date',parse_dates=True,
            usecols=['Date', 'Adj Close'], na_values=['nan'])
        df_temp = df_temp.rename(columns={'Adj Close': symbol})
        df = df.join(df_temp,how='left')
        if symbol == 'SPY':
            df = df.dropna(subset=['SPY'])
    return df

def test_run():
    dates = pd.date_range("2010-01-22", "2010-01-26")
    symbols = ['GOOG', 'IBM', 'GLD']
    symbols.sort()
    df = get_data(symbols, dates)
    print(df)

if __name__ == "__main__":
    test_run()