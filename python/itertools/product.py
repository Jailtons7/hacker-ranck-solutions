"""
This tool computes the cartesian product of input iterables.
It is equivalent to nested for-loops.
For example, product(A, B) returns the same as ((x,y) for x in A for y in B).

Example:
    A = [1, 2]
    B = [3, 4]

    AxB = [(1, 3), (1, 4), (2, 3), (2, 4)]
"""
from typing import Tuple, List, Union
from itertools import product


def cartesian_product(iterable: Union[List[List[int]], Tuple[List[int]]]) -> str:
    """ This function computes the cartesian product of iterable. """
    return " ".join(map(str, product(*iterable)))


if __name__ == "__main__":
    arr = []
    for _ in range(2):
        arr.append(list(map(int, input().split())))

    print(cartesian_product(arr))
