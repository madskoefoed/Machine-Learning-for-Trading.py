# Lesson 4.12 - Locate maximum value
import numpy as np

def get_max_index(a):
    return a.argmax()

def test_run():
    a = np.array([9, 6, 2, 3, 12, 14, 7, 10], dtype = np.int32)
    print("Array:\n", a)

    print("Maximum value:", a.max())
    print("Index of maximum:", get_max_index(a))

if __name__ == "__main__":
    test_run()