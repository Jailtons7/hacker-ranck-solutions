"""
You are given a spreadsheet that contains a list of athletes and their details (such as age, height, weight and so on).
You are required to sort the data based on the k-th attribute and print the final resulting table.
Follow the example given below for better understanding.

Sample Input
5 3
10 2 5
7 1 0
9 9 9
1 23 12
6 5 9
1

Sample Output
7 1 0
10 2 5
6 5 9
9 9 9
1 23 12

Explanation
The details are sorted based on the second attribute, since k is zero-indexed
"""
from typing import List


def _sort(iterable: List[List[int]], key: int) -> list:
    return sorted(iterable, key=lambda item: item[key])


if __name__ == '__main__':
    n, m = list(map(int, input().split()))
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())
    for row in _sort(iterable=arr, key=k):
        print(" ".join(list(map(str, row))))
