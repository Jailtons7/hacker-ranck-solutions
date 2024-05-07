"""
You are given a string S. Suppose a character 'c' occurs consecutively X times in the string.
Replace these consecutive occurrences of the character 'c' with (X, c) in the string.

Sample Input:
1222311

Sample Output:
(1, 1) (3, 2) (1, 3) (2, 1)

Explanation:
First, the character 1 occurs only once. It is replaced by (1, 1).
Then the character 2 occurs three times, and it is replaced by (3, 2) and so on.
"""
from typing import Sequence, List, Tuple
from itertools import groupby


def compress_string(seq: Sequence) -> List[Tuple[int, int]]:
    groups = groupby(seq, lambda x: x)
    result = []
    for key, group in groups:
        result.append((len(list(group)), int(key)))
    return result


if __name__ == '__main__':
    s = input()
    for group in compress_string(s):
        print(group, end=" ")
