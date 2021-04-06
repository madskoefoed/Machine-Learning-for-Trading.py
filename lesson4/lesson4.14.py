# Lesson 4.14 - How fast is NumPy?
import numpy as np
from time import time

# Execute function with given arguments and measure execution time
def how_long(func, *args):
    t0 = time()
    result = func(*args)
    t1 = time()
    return result, t1-t0

# Compute mean of all elements in the given 2D array
def manual_mean(arr):
    sum = 0
    for i in range(0, arr.shape[0]):
        for j in range(0, arr.shape[1]):
            sum += arr[i, j]
    return sum / arr.size

def numpy_mean(arr):
    return arr.mean()

def test_run():
    nd1 = np.random.random((1000, 10000))

    res_manual, t_manual = how_long(manual_mean, nd1)
    res_numpy, t_numpy = how_long(numpy_mean, nd1)

    print("Manual: {:.6f} ({:.3f} secs.) vs. NumPy: {:.6f} ({:.3f} secs.)".format(res_manual, t_manual, res_numpy, t_numpy))

    assert abs(res_manual - res_numpy) <= 10-6, "Results aren't equal"

    speedup = t_manual / t_numpy
    print("NumPy mean is ", speedup, " faster than manual for loops.")

if __name__ == "__main__":
    test_run()