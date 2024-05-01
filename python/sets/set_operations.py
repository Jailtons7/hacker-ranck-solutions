"""
The task is to perform commands over a given set and, at the end,
print the sum of the remaining elements.
The commands will be pop, remove and discard.

Input Format

The first line contains integer n, the number of elements in the set s.
The second line contains n space separated elements of set s.
All the elements are non-negative integers, less than or equal to 9.
The third line contains integer m, the number of commands.
The next m lines contains either pop, remove and/or discard commands followed by their associated value.

Sample Input
9
1 2 3 4 5 6 7 8 9
10
pop
remove 9
discard 9
discard 8
remove 7
pop
discard 6
remove 5
pop
discard 5

Sample Output
4
"""

from typing import Set


def perform_operation(set_: Set[int], command: str) -> Set[int]:
    split_ = command.split(" ")
    if len(split_) == 1:
        operation = split_[0]
        method = getattr(set_, operation)
        method()
    else:
        operation, value = command.split()[0], int(command.split()[1])
        method = getattr(set_, operation)
        method(value)
    return set_


if __name__ == '__main__':
    n = int(input())
    int_set = set(map(int, input().split()))
    commands = int(input())
    for _ in range(commands):
        int_set = perform_operation(set_=int_set, command=input())
    print(sum(int_set))
