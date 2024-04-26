"""
You are given the shape of the array in the form of space-separated integers,
each integer representing the size of different dimensions,
your task is to print an array of the given shape and integer type using the tools
numpy.zeros and numpy.ones.

Sample Input
2 2

Sample Output
[[0 0]
 [0 0]]
[[1 1]
 [1 1]]
"""
import typing
import numpy as np


def zeros_and_ones(shape: typing.Tuple[int, ...]) -> typing.Tuple[np.ndarray, np.ndarray]:
    return np.zeros(shape, dtype=int), np.ones(shape, dtype=int)


if __name__ == "__main__":
    shape_ = tuple(map(int, input().strip().split()))
    for array in zeros_and_ones(shape=shape_):
        print(array)
