# Lesson 4.10 - Array attributes
import numpy as np

def test_run():
    a = np.random.random((5, 4))
    print(a)
    print(a.shape)
    print("Rows:", a.shape[0])
    print("Columns:", a.shape[1])
    print("Number of dimensions:", len(a.shape))
    print("Number of elements:", a.size)
    print("Data type:", a.dtype)

if __name__ == "__main__":
    test_run()