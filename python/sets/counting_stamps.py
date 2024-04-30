"""
Rupal has a huge collection of country stamps.
She decided to count the total number of distinct country stamps in her collection.
She asked for your help.
You pick the stamps one by one from a stack of country stamps.

Find the total number of distinct country stamps.

Sample Input:
7
UK
China
USA
France
New Zealand
UK
France

Sample Output:
5
"""


if __name__ == '__main__':
    s = set()
    n = int(input())
    for _ in range(n):
        s.add(input())
    print(len(s))
