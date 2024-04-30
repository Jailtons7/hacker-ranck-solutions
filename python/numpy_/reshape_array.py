"""
You are given a space separated list of nine integers.
Your task is to convert this list into a 3x3 NumPy array.

Sample Input
1 2 3 4 5 6 7 8 9

Sample Output
[[1 2 3]
 [4 5 6]
 [7 8 9]]
"""

import numpy as np


def reshape_array(array: np.ndarray) -> np.ndarray:
    return array.reshape((3, 3))


if __name__ == '__main__':
    lst = list(map(int, input().rstrip().split()))
    arr = np.array(lst)
    print(reshape_array(array=arr))
