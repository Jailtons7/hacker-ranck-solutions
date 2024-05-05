"""
You are given a 2-D array of size NxM.
Your task is to find and print:

    The mean along axis 1
    The variation along axis 0
    The standard deviation along axis None

Sample Input:
2 2
1 2
3 4

Sample Output:
[ 1.5  3.5]
[ 1.  1.]
1.11803398875
"""
import numpy as np


def print_mean_variation_std_deviation(array: np.ndarray) -> None:
    mean = np.mean(array, axis=1)
    var = np.var(array, axis=0)
    std = np.std(array, axis=None)
    print(f"{mean}\n{var}\n{round(std, 11)}")


if __name__ == "__main__":
    n, m = map(int, input().split())
    lst = []
    for _ in range(n):
        lst.append(list(map(float, input().split())))

    arr = np.array(lst)
    print_mean_variation_std_deviation(array=arr)
