import numpy as np


def inner(first: np.ndarray, second: np.ndarray) -> int:
    return np.inner(first, second)


def outer(first: np.ndarray, second: np.ndarray) -> np.ndarray:
    return np.outer(first, second)


if __name__ == "__main__":
    a = np.array(list(map(int, input().strip().split())))
    b = np.array(list(map(int, input().strip().split())))

    print(inner(a, b))
    print(outer(a, b))
