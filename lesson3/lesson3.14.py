# Lesson 3.14 - More slicing
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
    dates = pd.date_range("2010-01-01", "2010-12-31")
    symbols = ['GOOG', 'IBM', 'GLD']
    df = get_data(symbols, dates)
    print(df.loc['2010-01-01':'2010-01-31'])
    print(df['GOOG'])
    print(df[['IBM', 'GLD']])
    print(df.loc['2010-03-10':'2010-03-15', ['SPY', 'IBM']])

if __name__ == "__main__":
    test_run()