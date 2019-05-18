#!/usr/bin/env python3
"""Loops
- Task: Read an integer . For all non-negative integers , print . See the sample for details.
- Input Format
The first and only line contains the integer, N.
- Constraints
1 <= N <= 20
- Output Format
Print N lines, one corresponding to each i.
- Sample Input 0
    5
- Sample Output 0
    0
    1
    4
    9
    16
"""
if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        print(i * i)

