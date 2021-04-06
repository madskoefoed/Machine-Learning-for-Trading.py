# Lesson 4.16 - Modifying array elements
import numpy as np

def test_run():
    a = np.random.rand(5, 4)
    print("Array:\n", a)

    a[0, 0] = 1
    print("Modified array:\n", a)

    a[0, :] = 2
    print("Modified (replaced a row with a single value):\n", a)

    a[:, 3] = [1, 2, 3, 4, 5]
    print("Modified (replaced a column with a list):\n", a)

if __name__ == "__main__":
    test_run()