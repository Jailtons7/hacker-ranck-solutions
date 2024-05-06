"""
You are given an integer N followed by N email addresses.
Your task is to print a list containing only valid email addresses in lexicographical order.

Valid email addresses must follow these rules:

    It must have the username@websitename.extension format type.
    The username can only contain letters, digits, dashes and underscores.
    The website name can only have letters and digits.
    The extension can only contain letters.
    The maximum length of the extension is 3.

Sample Input:
4
lara@hackerrank.com
brian-23@hackerrank.com
britts_54@hackerrank.com
@something.com

Sample Output:
['brian-23@hackerrank.com', 'britts_54@hackerrank.com', 'lara@hackerrank.com']
"""

import re
import typing


# The names of the functions below were provided by the problem editors
def fun(s: str) -> bool:
    pattern = re.compile(r"^([a-zA-Z0-9\-_]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3})$")
    return bool(pattern.fullmatch(string=s))


def filter_mail(emails: typing.List[str]) -> typing.List[str]:
    return list(filter(fun, emails))


if __name__ == "__main__":
    n = int(input())
    emails = [input() for _ in range(n)]

    filtered_emails = filter_mail(emails)
    filtered_emails.sort()
    print(filtered_emails)
