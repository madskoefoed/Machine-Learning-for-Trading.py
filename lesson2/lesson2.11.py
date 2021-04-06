import pandas as pd

# Lesson 2.11 - Mean volume
def get_mean_volume(symbol):
    df = pd.read_csv("c:/Code/Python/Udacity/data/{}.csv".format(symbol))
    return df['Volume'].mean()

def test_run():
    for symbol in ['AAPL', 'IBM']:
        print("Mean volume")
        print(symbol, get_mean_volume(symbol), '\n')

if __name__ == "__main__":
    test_run()