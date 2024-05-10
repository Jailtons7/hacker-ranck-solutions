"""
Task:

You are given three integers: a, b, and m. Print two lines.
On the first line, print a power b. On the second line, print a power b module m.
"""
from typing import Tuple


def power_and_module(a: int, b: int, m: int) -> Tuple[int, int]:
    return pow(a, b), pow(a, b, m)


if __name__ == '__main__':
    a_, b_, m_ = int(input()), int(input()), int(input())
    print("\n".join(map(str, power_and_module(a=a_, b=b_, m=m_))))
