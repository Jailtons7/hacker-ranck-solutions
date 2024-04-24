"""
Given the names and grades for each student in a class of students,
store them in a nested list and print the name(s) of any student(s) having the second-lowest grade.

Note: If there are multiple students with the second-lowest grade,
order their names alphabetically and print each name on a new line.

Example
records = [["chi", 20.0], ["beta", 50.0], ["alpha", 50.0]]
The ordered list of scores is [20.0, 50.0], so the second-lowest score is 50.0.
There are two students with that score ["beta", "alpha"].

Ordered alphabetically, the names are printed as:

alpha
beta

Input Format

The first line contains an integer n, the number of students.,
The subsequent lines describe each student over lines.
    - The first line contains a student's name.
    - The second line contains their grade.

Constraints:
    There will always be one or more students having the second-lowest grade.

Output Format
    Print the name(s) of any student(s) having the second-lowest grade in.
    If there are multiple students, order their names alphabetically and print each one on a new line.

Sample Input 0

5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39

Sample Output 0

Berry
Harry

"""

import operator
from typing import List


def solve(records: List[List[str | float]]) -> List[str]:
    """
    :param records: a list of lists with names and grades
    :return: a list of student names having the second-lowest grade ordered by name
    """
    records.sort(key=operator.itemgetter(1, 0))
    unique_records = list(set([record[1] for record in records]))
    unique_records.sort()
    seconds = [record[0] for record in records if record[1] == unique_records[1]]
    seconds.sort()
    return seconds


if __name__ == '__main__':
    records_ = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records_.append([name, score])

    print("\n".join(solve(records=records_)))
