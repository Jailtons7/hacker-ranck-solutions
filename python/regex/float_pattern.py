"""
You are given a string N.
Your task is to verify that N is a floating point number.
In this task, a valid float number must satisfy all the following requirements:

Number can start with +, - or . symbol.
For example:
✔+4.50
✔-1.0
✔.5
✔-.7
✔+.4
✖ -+4.5

Number must contain at least 1 decimal value.
For example:
✖ 12.
✔12.0

Number must have exactly one . (dot) symbol.
Number must not give any exceptions when converted using float(N).

Sample Input:
4
4.0O0
-1.00
+4.54
SomeRandomStuff

Sample Output:
False
True
True
False

Note:
4.0O0 is not a valid number, it has the letter O
"""
from typing import List
import re


def detect_valid_float(numbers: List[str]) -> List[str]:
    pattern = re.compile(r"[+-]?\d*\.\d+")
    return [str(bool(pattern.fullmatch(number))) for number in numbers]


if __name__ == "__main__":
    n = int(input())
    float_numbers = [input() for i in range(n)]
    print("\n".join(detect_valid_float(float_numbers)))
