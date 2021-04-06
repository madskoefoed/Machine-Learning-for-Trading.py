# Lesson 4.11 - Operations on ndarrays
import numpy as np

def test_run():
    np.random.seed(693)
    a = np.random.randint(0, 10, size=(5, 4))
    print("Array:\n", a)
    print("Sum:", a.sum())
    print("Sum of each column", a.sum(axis = 0))
    print("Sum of each row", a.sum(axis = 1))
    print("Minimum:", a.min(axis = 0))
    print("Maximum:", a.max(axis = 1))
    print("Mean of all elements:", a.mean())

if __name__ == "__main__":
    test_run()