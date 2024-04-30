"""
You are given a 2-D array with dimensions n x m.
Your task is to perform the min function over axis 1 and then find the max of that.

Sample Input
4 2
2 5
3 7
1 3
4 0

Sample Output
3

"""

import numpy as np


def min_and_max(arr: np.ndarray) -> int:
    min_ = np.min(a=arr, axis=1)
    return np.max(a=min_)


if __name__ == '__main__':
    n, m = map(int, input().rstrip().split())
    lst = []
    for _ in range(n):
        row = list(map(int, input().rstrip().split()))
        lst.append(row)
    arr_ = np.array(lst)
    print(min_and_max(arr=arr_))
