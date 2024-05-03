"""
You are given a string S.
S contains alphanumeric characters only.

Your task is to sort the string in the following manner:
    All sorted lowercase letters are ahead of uppercase letters.
    All sorted uppercase letters are ahead of digits.
    All sorted odd digits are ahead of sorted even digits.

Sample Input:
Sorting1234

Sample Output:
ginortS1324

"""

import re


def sort_alphanumeric(string: str) -> str:
    lowercase_pattern = re.compile(r'[a-z]+')
    uppercase_pattern = re.compile(r'[A-Z]+')
    odd_numbers_pattern = re.compile(r'[13579]')
    even_numbers_pattern = re.compile(r'[02468]')
    lowercase = lowercase_pattern.findall(string)
    uppercase = uppercase_pattern.findall(string)
    odd_numbers = odd_numbers_pattern.findall(string)
    even_numbers = even_numbers_pattern.findall(string)
    sorted_lower = sorted("".join(lowercase))
    sorted_upper = sorted("".join(uppercase))
    sorted_odd_num = sorted("".join(odd_numbers))
    sorted_even_num = sorted("".join(even_numbers))
    return "".join(sorted_lower) + "".join(sorted_upper) + "".join(sorted_odd_num) + "".join(sorted_even_num)


if __name__ == '__main__':
    string_ = input()
    print(sort_alphanumeric(string_))
