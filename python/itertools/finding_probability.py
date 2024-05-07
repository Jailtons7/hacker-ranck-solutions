"""
You are given a list of N lowercase English letters.
For a given integer K, you can select any indices (assume
1-based indexing) with a uniform probability from the list.

Find the probability that at least one of the k indices selected
will contain the letter: 'a'.

Input Format:
The first line contains the integer N. Denoting the length of the list
The second the space-separated lowercase English letters.
The third line contains the integer K. Denoting the length of the samples

Sample Input:
4
a a c d
2

Sample Output:
0.8333
"""
from typing import Sequence
from itertools import combinations


def get_probability(iterable: Sequence[str], k_: int) -> float:
    """
    returns the probability of finding at least one letter "a"
    in a set of combinations with size "k_" of the given iterable
    """
    subsets = combinations(iterable, k_)
    count = total = 0
    for subset in subsets:
        if "a" in subset:
            count += 1
        total += 1
    return count / total


if __name__ == '__main__':
    n = int(input())
    letters = list(input().split())
    k = int(input())

    print(round(get_probability(letters, k), 4))
