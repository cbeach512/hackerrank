#!/usr/bin/env python3
"""Lists
Consider a list (list = []). You can perform the following commands:
  - insert i e: Insert integer e at position i.
  - print: Print the list.
  - remove e: Delete the first occurrence of integer e.
  - append e: Insert integer e at the end of the list.
  - sort: Sort the list.
  - pop: Pop the last element from the list.
  - reverse: Reverse the list.
Initialize your list and read in the value of n followed by n lines of commands where each command will be of the 7 types listed above. Iterate through each command in order and perform the corresponding operation on your list.
- Input Format
The first line contains an integer, n, denoting the number of commands.
Each line i of the n subsequent lines contains one of the commands described above.
- Constraints
  - The elements added to the list must be integers.
- Output Format
For each command of type print, print the list on a new line.
- Sample Input 0
    12
    insert 0 5
    insert 1 10
    insert 0 6
    print
    remove 6
    append 9
    append 1
    sort
    print
    pop
    reverse
    print
- Sample Output 0
    [6, 5, 10]
    [1, 5, 9, 10]
    [9, 5, 1]
"""
class Listy():
    def __init__(self):
        self.l = []

    def cmd_runner(self, cmd, args):
        try:
            getattr(self, '_{}'.format(cmd))(args)
        except TypeError:
            getattr(self, '_{}'.format(cmd))()

    def _insert(self, args):
        i, e = args
        self.l.insert(i, e)

    def _print(self):
        print(self.l)

    def _remove(self, args):
        self.l.remove(args[0])

    def _append(self, args):
        self.l.append(args[0])

    def _sort(self):
        self.l.sort()

    def _pop(self):
        self.l.pop()

    def _reverse(self):
        self.l.reverse()

if __name__ == '__main__':
    N = int(input())
    commands = []
    for _ in range(N):
        inputs = input().split()
        cmd = {'cmd': inputs[0], 'args': [int(i) for i in inputs[1:]]}
        commands.append(cmd)
    listy = Listy()
    lrun = listy.cmd_runner
    for cmd in commands:
        lrun(cmd['cmd'], cmd['args'])

