"""
You are given a string s.
Your task is to print all possible permutations of size k of the string in lexicographic sorted order.

Sample Input:
HACK 2

Sample Output:
AC
AH
AK
CA
CH
CK
HA
HC
HK
KA
KC
KH
"""

from itertools import permutations


def perform_permutations(s: str, k_: int) -> str:
    """
    :param s: a string
    :param k_: the size of permutations
    :return: a \n separated string of all possible permutations of size k_ of the string
    """
    return "\n".join(map(lambda tuple_: "".join(tuple_), permutations(s, k_)))


if __name__ == '__main__':
    string, k = input().split()
    string = "".join(sorted(string))
    print(perform_permutations(string, int(k)))
