"""
The task is to print an array of size NxM with its main diagonal elements as 1's and 0's everywhere else.

Sample Input:
3 3

Sample Output:
[[ 1.  0.  0.]
 [ 0.  1.  0.]
 [ 0.  0.  1.]]

"""

import numpy as np


def identity(n, m, k=0) -> np.ndarray:
    return np.eye(N=n, M=m, k=k, dtype=np.double)


if __name__ == '__main__':
    np.set_printoptions(legacy='1.13')
    N, M = map(int, input().rstrip().split())
    print(identity(N, M, k=0))
