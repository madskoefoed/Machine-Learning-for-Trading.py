import pandas as pd
import matplotlib.pyplot as plt

# Lesson 2.14 - Plot two columns
def test_run():
    df = pd.read_csv('c:/Code/Python/Udacity/data/AAPL.csv')
    df[['Close', 'Adj Close']].plot()
    plt.show()

if __name__ == "__main__":
    test_run()