"""
You are given a positive integer N, 1 <= N <= 9.
Print a numerical triangle of height (N - 1) like the one below:

1
22
333
4444
55555
......

Can you do it using only arithmetic operations, a single for loop and print statement?
Use no more than two lines and using anything related to strings will give you a score of 0.

Sample Input:
5

Sample Output:
1
22
333
4444
"""

for i in range(1, int(input())):
    print(int(i * 10 ** i / 9))
