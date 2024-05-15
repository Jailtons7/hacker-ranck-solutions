import numpy as np


def print_operations(first: np.ndarray, second: np.ndarray) -> None:
    print(first + second)
    print(first - second)
    print(first * second)
    print(first // second)
    print(first % second)
    print(first ** second)


if __name__ == '__main__':
    n, m = map(int, input().split())
    list_a = [list(map(int, input().split())) for _ in range(n)]
    list_b = [list(map(int, input().split())) for _ in range(n)]
    a = np.array(list_a)
    b = np.array(list_b)
    print_operations(a, b)
