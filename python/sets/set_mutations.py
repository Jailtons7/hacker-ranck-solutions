"""
TASK:
You are given a set A and N number of other sets.
These N number of sets have to perform some specific mutation operations on set A.

Your task is to execute those operations and print the sum of elements from set A.

Sample Input:
 16
 1 2 3 4 5 6 7 8 9 10 11 12 13 14 24 52
 4
 intersection_update 10
 2 3 5 6 8 9 1 4 7 11
 update 2
 55 66
 symmetric_difference_update 5
 22 7 35 62 58
 difference_update 7
 11 22 35 55 58 62 66

Sample Output:
38
"""
from typing import Set


def perform_mutation(mutation: str, first: Set[int], second: Set[int]) -> Set[int]:
    method = getattr(first, mutation)
    return method(second)


if __name__ == '__main__':
    n = int(input())
    a = set(map(int, input().split()))
    number_operations = int(input())
    for _ in range(number_operations):
        operation_, m = input().split()
        b = set(map(int, input().split()))
        perform_mutation(operation_, a, b)
    print(sum(a))
