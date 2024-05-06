"""
Given a list of rational numbers, find their product and print its simplified form

Input Format:
First line contains n, the number of rational numbers.
The i-th of next n lines contain two integers each, the numerator(Ni) and denominator(Di)
of the i-th rational number in the list.

Sample Input:
3
1 2
3 4
10 6

Sample Output:
5 8
"""
from fractions import Fraction
from functools import reduce
from typing import List, Tuple


def product(fracs_: List[Fraction]) -> Tuple[int, int]:
    t = reduce(lambda a, b: a * b, fracs_)
    return t.numerator, t.denominator


if __name__ == '__main__':
    fracs = []
    for _ in range(int(input())):
        fracs.append(Fraction(*map(int, input().split())))
    result = product(fracs)
    print(*result)
