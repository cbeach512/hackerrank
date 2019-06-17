#!/usr/bin/env python3
"""Piling Up!
There is a horizontal row of n cubes. The length of each cube is given. You need to create a new vertical pile of cubes. The new pile should follow these directions: if cubei is on top of cubej then sideLengthj >= sideLengthi.
When stacking the cubes, you can only pick up either the leftmost or the rightmost cube each time. Print "Yes" if it is possible to stack the cubes. Otherwise, print "No". Do not print the quotation marks.
- Input Format
The first line contains a single integer T, the number of test cases.
For each test case, there are 2 lines.
The first line of each test case contains n, the number of cubes.
The second line contains n space separated integers, denoting the sideLengths of each cube in that order.
- Constraints
1 <= T <= 5
1 <= n <= 10^5
1 <= sideLength < 2^31
- Output Format
For each test case, output a single line containing either "Yes" or "No" without the quotes.
- Sample Input
    2
    6
    4 3 2 1 3 4
    3
    1 3 2
- Sample Output
    Yes
    No
- Explanation
In the first test case, pick in this order: left - 4, right - 4, left - 3, right - 3, left - 2, right - 1.
In the second test case, no order gives an appropriate arrangement of vertical cubes. 3 will always come after either 1 or 2.
"""
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque


def stacker():
    n = int(input())
    d = deque(map(int, input().split()))
    if n < 3:
        return 'Yes'
    stack = list()
    for _ in range(n):
        if d[-1] >= d[0]:
            stack.append(d.pop())
        else:
            stack.append(d.popleft())
        try:
            if stack[-1] > stack[-2]:
                return 'No'
        except IndexError:
            pass
    return 'Yes'


def main():
    t = int(input())
    for _ in range(t):
        print(stacker())


if __name__ == '__main__':
    main()

