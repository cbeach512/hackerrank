#!/usr/bin/env python3
"""Designer door mat
Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications:
  - Mat size must be NxM. (N is an odd natural number, and M is 3 times N.)
  - The design should have 'WELCOME' written in the center.
  - The design pattern should only use |, . and - characters.
- Sample Designs
  - Size: 7 x 21
    ---------.|.---------
    ------.|..|..|.------
    ---.|..|..|..|..|.---
    -------WELCOME-------
    ---.|..|..|..|..|.---
    ------.|..|..|.------
    ---------.|.---------
  - Size: 11 x 33
    ---------------.|.---------------
    ------------.|..|..|.------------
    ---------.|..|..|..|..|.---------
    ------.|..|..|..|..|..|..|.------
    ---.|..|..|..|..|..|..|..|..|.---
    -------------WELCOME-------------
    ---.|..|..|..|..|..|..|..|..|.---
    ------.|..|..|..|..|..|..|.------
    ---------.|..|..|..|..|.---------
    ------------.|..|..|.------------
    ---------------.|.---------------
- Input Format
A single line containing the space separated values of N and M.
- Constraints
5 < N < 101
15 < M < 303
- Output Format
Output the design pattern.
- Sample Input
    9 27
- Sample Output
    ------------.|.------------
    ---------.|..|..|.---------
    ------.|..|..|..|..|.------
    ---.|..|..|..|..|..|..|.---
    ----------WELCOME----------
    ---.|..|..|..|..|..|..|.---
    ------.|..|..|..|..|.------
    ---------.|..|..|.---------
    ------------.|.------------
"""
# Enter your code here. Read input from STDIN. Print output to STDOUT
def debug(msg, var=None):
    dmsg = msg.format(var)
    print('DEBUG: {}'.format(dmsg))

class Mat():
    _fill = '-'
    _design = '.|.'

    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.half_n = n // 2

    def _welcome(self):
        msg = 'WELCOME'.center(self.m, self._fill)
        return msg

    def _top(self):
        lines = [(self._design * (1 + i * 2)).center(self.m, self._fill) for i in range(self.half_n)]
        msg = '\n'.join(lines)
        return msg

    def _bottom(self):
        lines = [(self._design * (1 + (self.half_n -1 - i) * 2)).center(self.m, self._fill) for i in range(self.half_n)]
        msg = '\n'.join(lines)
        return msg

    def print(self):
        mat = '\n'.join([self._top(), self._welcome(), self._bottom()])
        print(mat)


if __name__ == '__main__':
    n, m = (int(i) for i in input().split()) # normal input from cli disabled durring dev
    mat = Mat(n, m)
    mat.print()

