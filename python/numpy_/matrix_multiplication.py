"""
You are given two arrays A and B. Both have dimensions of NXN.
Your task is to compute their matrix product.

Sample Input
2
1 2
3 4
1 2
3 4

Sample Output
[[ 7 10]
 [15 22]]
"""
import numpy as np


def matrix_multiplication(first: np.ndarray, second: np.ndarray) -> np.ndarray:
    return np.matmul(first, second)


if __name__ == '__main__':
    n = int(input())
    lst1 = []
    lst2 = []
    for _ in range(n):
        lst1.append(list(map(int, input().split())))

    for _ in range(n):
        lst2.append(list(map(int, input().split())))

    arr1 = np.array(lst1)
    arr2 = np.array(lst2)

    print(matrix_multiplication(arr1, arr2))
