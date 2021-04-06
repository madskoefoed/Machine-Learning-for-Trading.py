# Lesson 4.9 - Generating random numbers
import numpy as np

def test_run():
    print("Uniform(0, 1)")
    print(np.random.random((5, 4)))
    print("Uniform(0, 1) without tuple")
    print(np.random.rand(5, 4))
    print("N(0, 1)")
    print(np.random.normal(size=(2, 3)))
    print("N(50, 10^2)")
    print(np.random.normal(50, 10, size=(2, 3)))
    print("Random integers")
    print(np.random.randint(10))
    print(np.random.randint(0, 10))
    print(np.random.randint(0, 10, size=5))
    print(np.random.randint(0, 10, size=(2, 3)))

if __name__ == "__main__":
    test_run()