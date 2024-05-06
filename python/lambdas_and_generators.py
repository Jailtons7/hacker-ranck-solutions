"""
You have to generate the first N fibonacci numbers, 0 being the first.
Then, apply the map function and a lambda expression to cube each fibonacci number and print the list.

Sample Input:
5

Sample Output:
[0, 1, 1, 8, 27]
"""
from typing import Generator


cube = lambda x: x ** 3


def fibonacci(number: int) -> Generator[int, None, None]:
    a, b = 0, 1
    for _ in range(number):
        yield a
        a, b = b, a + b


if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
