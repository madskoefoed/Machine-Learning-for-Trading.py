import pandas as pd

# Lesson 2.10 - Max closing prince
def get_max_close(symbol):
    df = pd.read_csv("c:/Code/Python/Udacity/data/{}.csv".format(symbol))
    return df['Close'].max()

def test_run():
    for symbol in ['AAPL', 'IBM']:
        print("Max close")
        print(symbol, get_max_close(symbol), '\n')

if __name__ == "__main__":
    test_run()