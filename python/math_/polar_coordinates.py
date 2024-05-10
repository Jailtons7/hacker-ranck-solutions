"""
Task:
You are given a complex Z. Your task is to convert it to polar coordinates.
Note: The output should be correct up to 3 decimal places.

Sample Input:
1+2j

Sample Output:
2.236
1.107
"""
from typing import Tuple
from cmath import phase


def convert_to_polar(z: complex) -> Tuple[float, float]:
    """
    Convert a complex number z to a polar coordinates.
    :param z: a complex number in format a + bj (j is the imaginary unit)
    :return: a tuple of the polar coordinates, where the first element is the module
    and the second element is the phase
    """
    module = abs(z)
    phase_ = phase(z)
    return round(module, 3), round(phase_, 3)


if __name__ == "__main__":
    z_ = complex(input())
    print("\n".join(map(str, convert_to_polar(z=z_))))
