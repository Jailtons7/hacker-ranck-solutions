"""
Mr. Vincent works in a door mat manufacturing company.
One day, he designed a new door mat with the following specifications:

    - Mat size must be n x m. (n is an odd natural number, and m is 3 times n.)
    - The design should have 'WELCOME' written in the center.
    - The design pattern should only use "|", "." and "-" characters.

Sample design pattern:
7 21
---------.|.---------
------.|..|..|.------
---.|..|..|..|..|.---
-------WELCOME-------
---.|..|..|..|..|.---
------.|..|..|.------
---------.|.---------

11 33
---------------.|.---------------
------------.|..|..|.------------
---------.|..|..|..|..|.---------
------.|..|..|..|..|..|..|.------
---.|..|..|..|..|..|..|..|..|.---
-------------WELCOME-------------
---.|..|..|..|..|..|..|..|..|.---
------.|..|..|..|..|..|..|.------
---------.|..|..|..|..|.---------
------------.|..|..|.------------
---------------.|.---------------
"""


def perform_door_mat_design(height, width):
    middle = height // 2
    for i in range(height):
        if i < middle:
            print(((2 * i + 1) * ".|.").center(width, "-"))
        elif i == middle:
            print("WELCOME".center(width, "-"))
        else:
            print(((height - 2 * (i - middle)) * ".|.").center(width, "-"))


if __name__ == '__main__':
    n, m = map(int, input().split())
    perform_door_mat_design(n, m)
