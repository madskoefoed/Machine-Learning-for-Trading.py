# Lesson 4.19 - Arithmetic operations
import numpy as np

def test_run():
    a = np.array([(1, 2, 3, 4, 5), (10, 20, 30, 40, 50)])
    print("Original array a:\n", a)
    print("\nArray a multiplied by 2:\n", a*2)
    print("\nDivide a by 2:\n", a//2)
    print("\nDivide a by 2 (integer division):\n", a/2)

    b = np.array([(100, 200, 300, 400, 500), (1, 2, 3, 4, 5)])
    print("\nOriginal array b:\n", b)
    print("\nAdd a + a:\n", a + b)

    print("\Multiple a * b:\n", a * b)

    print("\nDivide a / b:\n", a / b)
    print("\nDivide a / b (integer division):\n", a // b)

if __name__ == "__main__":
    test_run()