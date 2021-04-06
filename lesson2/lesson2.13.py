import pandas as pd
import matplotlib.pyplot as plt

# Lesson 2.13 - Plot high prices for IBM
def test_run():
    df = pd.read_csv('c:/Code/Python/Udacity/data/IBM.csv')
    print(df['High'])
    df['High'].plot()
    plt.show()

if __name__ == "__main__":
    test_run()