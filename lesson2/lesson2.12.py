import pandas as pd
import matplotlib.pyplot as plt

# Lesson 2.12 - Plotting stock price data
def test_run():
    df = pd.read_csv('c:/Code/Python/Udacity/data/AAPL.csv')
    print(df['Adj Close'])
    df['Adj Close'].plot()
    plt.show()

if __name__ == "__main__":
    test_run()