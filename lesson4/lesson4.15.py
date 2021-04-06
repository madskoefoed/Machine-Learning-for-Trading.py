# Lesson 4.15 - Accessing array elements
import numpy as np

def test_run():
    a = np.random.rand(5, 4)
    print("Array:\n", a)
    element = a[3, 2]
    print(element)

    print("Column slicing:", a[0, 1:3])

    print("Row and column slicing:\n", a[0:2, 0:2])

    print("Step slicing:\n", a[:, 0:3:2])

if __name__ == "__main__":
    test_run()