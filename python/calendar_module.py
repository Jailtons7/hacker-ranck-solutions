"""
You are given a date. Your task is to find what the day is on that date.

Input Format:
A single line of input containing the space separated month, day and year, respectively, in mm-dd-yyyy format.

Sample Input:
08 05 2015

Sample Output:
WEDNESDAY
"""
import calendar


if __name__ == "__main__":
    mm, dd, yyyy = map(int, input().strip().split())
    day = calendar.weekday(yyyy, mm, dd)
    print(calendar.day_name[day].upper())
