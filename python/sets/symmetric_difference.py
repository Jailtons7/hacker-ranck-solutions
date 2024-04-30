"""
Given sets of integers, m and n, print their symmetric difference in ascending order.
The term symmetric difference indicates those values that exist in either m or n but do not exist in both.

Sample Input:

STDIN       Function
-----       --------
4           set a size M = 4
2 4 5 9     a = {2, 4, 5, 9}
4           set b size N = 4
2 4 11 12   b = {2, 4, 11, 12}

Sample Output:

5
9
11
12
"""

import typing


def symmetric_difference(first: typing.Set[int], second: typing.Set[int]) -> typing.List[int]:
    """ return the ordered symmetric difference between two sets. """
    diff = set()
    diff.update(first.difference(second))
    diff.update(second.difference(first))
    ordered_diff = sorted(list(diff))
    return ordered_diff


if __name__ == '__main__':
    n = int(input())
    first_lst = set(map(int, input().strip().split()))
    m = int(input())
    second_lst = set(map(int, input().strip().split()))
    print("\n".join(list(map(str, symmetric_difference(first=first_lst, second=second_lst)))))
