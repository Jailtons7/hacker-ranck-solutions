"""
You are given a 1-D array, A.
Your task is to print the floor, ceil and rint of all the elements of A.
Note:
In order to get the correct output format, add the line below the numpy import.
"np.set_printoptions(legacy='1.13')"

Sample Input:
1.1 2.2 3.3 4.4 5.5 6.6 7.7 8.8 9.9

Sample Output:
[ 1.  2.  3.  4.  5.  6.  7.  8.  9.]
[  2.   3.   4.   5.   6.   7.   8.   9.  10.]
[  1.   2.   3.   4.   6.   7.   8.   9.  10.]
"""

import numpy as np
np.set_printoptions(legacy='1.13')


def arr_floor_ceil_rint(array: np.ndarray) -> None:
    print(np.floor(array))
    print(np.ceil(array))
    print(np.rint(array))


if __name__ == '__main__':
    arr = np.array(list(map(float, input().strip().split())))
    arr_floor_ceil_rint(array=arr)
