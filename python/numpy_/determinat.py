"""
You are given a square matrix A with dimensions X.
Your task is to find the determinant. Note: Round the answer to 2 places after the decimal.

Sample Input:
2
1.1 1.1
1.1 1.1

Sample Output:
0.0
"""
import numpy as np


def get_determinant(matrix: np.ndarray) -> float:
    return round(np.linalg.det(matrix), 2)


if __name__ == '__main__':
    n = int(input())
    arr_ = np.array([list(map(float, input().split())) for _ in range(n)])
    print(arr_)
    print(get_determinant(matrix=arr_))
