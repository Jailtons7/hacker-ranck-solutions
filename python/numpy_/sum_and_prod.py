"""
You are given a 2-D array with dimensions N x M.
Your task is to perform the sum tool over axis 0 and then find the product of that result.

Sample Input
2 2
1 2
3 4

Sample Output
24
"""

import numpy as np


def sum(arr: np.ndarray) -> np.ndarray:
    return np.sum(arr, axis=0)


def sum_and_prod(arr: np.ndarray) -> int:
    sum_ = sum(arr)
    return np.prod(sum_)


if __name__ == '__main__':
    n, m = map(int, input().split())
    lst = []
    for _ in range(n):
        lst.append(list(map(int, input().split())))

    array = np.array(lst)
    print(sum_and_prod(arr=array))
