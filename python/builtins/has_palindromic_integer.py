"""
A palindromic number (also known as a numeral palindrome or a numeric palindrome) is a number (such as 16461)
that remains the same when its digits are reversed.

The task is:
You are given a space separated list of integers.
If all the integers are positive,
then you need to check if any integer is a palindromic integer.

Sample Input:
5
12 9 61 5 14

Sample Output:
True

Explanation:
All given numbers are positive integers and 9 and 5 are palindromic integer, so it prints True.
"""
from typing import List


def all_integers_positive(int_list: List[int]) -> bool:
    return all([x > 0 for x in int_list])


def has_palindromic_integer(str_list: List[str]) -> bool:
    return any([x == x[::-1] for x in str_list])


if __name__ == "__main__":
    n = int(input())
    str_input = input().strip().split()
    integers = list(map(int, str_input))
    if all_integers_positive(int_list=integers):
        print(has_palindromic_integer(str_list=str_input))
    else:
        print(False)
