# Lesson 4.17 - Indexing an array with another array
import numpy as np

def test_run():
    a = np.random.rand(5)
    indices = np.array([1, 1, 2, 3])
    print(a[indices])

if __name__ == "__main__":
    test_run()