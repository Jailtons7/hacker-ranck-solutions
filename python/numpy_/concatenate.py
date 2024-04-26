"""
You are given two integer arrays of size NxP and MxP (N and M are rows, and P is the column).
Your task is to concatenate the arrays along axis 0.

Sample Input
# N, M, P
4 3 2
# N rows of the first array with P columns
1 2
1 2
1 2
1 2
# M rows of the second array with P columns
3 4
3 4
3 4

Sample Output
# Two arrays concatenated along axis 0
[[1 2]
 [1 2]
 [1 2]
 [1 2]
 [3 4]
 [3 4]
 [3 4]]
"""

import numpy as np


if __name__ == '__main__':
    N, M, P = map(int, input().split())

    list_1 = []
    for _ in range(N):
        list_1.append(list(map(int, input().split())))

    list_2 = []
    for _ in range(M):
        list_2.append(list(map(int, input().split())))

    arr1 = np.array(list_1)
    arr2 = np.array(list_2)
    arr3 = np.concatenate((arr1, arr2), axis=0)
    print(arr3)
