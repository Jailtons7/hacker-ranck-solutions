"""
You are given two integer arrays, A and B of dimensions NxM.
Your task is to perform the following operations:

    Add
    Subtract
    Multiply
    Integer Division
    Mod
    Power

Sample Input:
1 4
1 2 3 4
5 6 7 8

Sample Output:
[[ 6  8 10 12]]
[[-4 -4 -4 -4]]
[[ 5 12 21 32]]
[[0 0 0 0]]
[[1 2 3 4]]
[[    1    64  2187 65536]]

"""
import numpy as np


def print_operations(first: np.ndarray, second: np.ndarray) -> None:
    print(first + second)
    print(first - second)
    print(first * second)
    print(first // second)
    print(first % second)
    print(first ** second)


if __name__ == '__main__':
    n, m = map(int, input().split())
    list_a = [list(map(int, input().split())) for _ in range(n)]
    list_b = [list(map(int, input().split())) for _ in range(n)]
    a = np.array(list_a)
    b = np.array(list_b)
    print_operations(a, b)
