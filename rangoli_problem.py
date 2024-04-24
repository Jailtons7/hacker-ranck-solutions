"""
You are given an integer,
Your task is to print an alphabet rangoli of size.
(Rangoli is a form of Indian folk art based on creation of patterns.)

Different sizes of alphabet rangoli are shown below:
#size 3

----c----
--c-b-c--
c-b-a-b-c
--c-b-c--
----c----

#size 5

--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------

#size 10

------------------j------------------
----------------j-i-j----------------
--------------j-i-h-i-j--------------
------------j-i-h-g-h-i-j------------
----------j-i-h-g-f-g-h-i-j----------
--------j-i-h-g-f-e-f-g-h-i-j--------
------j-i-h-g-f-e-d-e-f-g-h-i-j------
----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
--j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
j-i-h-g-f-e-d-c-b-a-b-c-d-e-f-g-h-i-j
--j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
------j-i-h-g-f-e-d-e-f-g-h-i-j------
--------j-i-h-g-f-e-f-g-h-i-j--------
----------j-i-h-g-f-g-h-i-j----------
------------j-i-h-g-h-i-j------------
--------------j-i-h-i-j--------------
----------------j-i-j----------------
------------------j------------------
"""


def insert_row(size: int, row: int, rangoli: list) -> str:
    sides = (2 * size - 2 - 2 * row) * "-"
    left = "-".join(rangoli[:row + 1])
    right = "-".join(rangoli[0:row][::-1])
    if right:
        center = left + "-" + right
    else:
        center = left
    return f"{sides}{center}{sides}"


def print_rangoli(size: int) -> None:
    alphabet = "a b c d e f g h i j k l m n o p q r s t u v w x y z".split()
    rangoli = alphabet[:size]
    rangoli.sort(reverse=True)
    # upper rangoli part
    for row in range(size):
        print(insert_row(size=size, row=row, rangoli=rangoli))
    # down rangoli part
    for row in range(size - 2, -1, -1):
        print(insert_row(size=size, row=row, rangoli=rangoli))


if __name__ == '__main__':
    size = int(input())
    print_rangoli(size)
