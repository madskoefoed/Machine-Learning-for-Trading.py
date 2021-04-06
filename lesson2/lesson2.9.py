import pandas as pd

# Lesson 2.9 - Select rows
def test_run():
    df = pd.read_csv('c:/Code/Python/Udacity/data/AAPL.csv')
    print(df[10:21], '\n')

if __name__ == "__main__":
    test_run()