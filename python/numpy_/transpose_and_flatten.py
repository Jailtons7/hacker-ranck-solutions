"""
You are given a NxM integer array matrix with space separated elements (N = rows and M = columns).
Your task is to print the transpose and flatten results.

Sample Input

2 2
1 2
3 4

Sample Output

[[1 3]
 [2 4]]
[1 2 3 4]

"""

import numpy as np


def transpose(array: np.ndarray) -> np.ndarray:
    return array.T


def flatten(array: np.ndarray) -> np.ndarray:
    return array.flatten()


def transpose_and_flatten(array) -> np.ndarray:
    transposed = transpose(array)
    return flatten(transposed)


if __name__ == '__main__':
    N, M = map(int, input().split())
    lst = []
    for _ in range(N):
        lst.append(list(map(int, input().split())))

    arr = np.array(lst)
    print(transpose(array=arr))
    print(flatten(array=arr))
