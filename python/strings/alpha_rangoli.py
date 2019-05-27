#!/usr/bin/env python3
"""Alphabet rangoli
You are given an integer, N. Your task is to print an alphabet rangoli of size N. (Rangoli is a form of Indian folk art based on creation of patterns.)
Different sizes of alphabet rangoli are shown below:
  - #size 3
    ----c----
    --c-b-c--
    c-b-a-b-c
    --c-b-c--
    ----c----
  - #size 5
    --------e--------
    ------e-d-e------
    ----e-d-c-d-e----
    --e-d-c-b-c-d-e--
    e-d-c-b-a-b-c-d-e
    --e-d-c-b-c-d-e--
    ----e-d-c-d-e----
    ------e-d-e------
    --------e--------
  - #size 10
    ------------------j------------------
    ----------------j-i-j----------------
    --------------j-i-h-i-j--------------
    ------------j-i-h-g-h-i-j------------
    ----------j-i-h-g-f-g-h-i-j----------
    --------j-i-h-g-f-e-f-g-h-i-j--------
    ------j-i-h-g-f-e-d-e-f-g-h-i-j------
    ----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
    --j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
    j-i-h-g-f-e-d-c-b-a-b-c-d-e-f-g-h-i-j
    --j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
    ----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
    ------j-i-h-g-f-e-d-e-f-g-h-i-j------
    --------j-i-h-g-f-e-f-g-h-i-j--------
    ----------j-i-h-g-f-g-h-i-j----------
    ------------j-i-h-g-h-i-j------------
    --------------j-i-h-i-j--------------
    ----------------j-i-j----------------
    ------------------j------------------
The center of the rangoli has the first alphabet letter a, and the boundary has the Nth alphabet letter (in alphabetical order).
- Input Format
Only one line of input containing N, the size of the rangoli.
- Constraints
0 < N < 27
- Output Format
Print the alphabet rangoli in the format explained above.
- Sample Input
    5
- Sample Output
    --------e--------
    ------e-d-e------
    ----e-d-c-d-e----
    --e-d-c-b-c-d-e--
    e-d-c-b-a-b-c-d-e
    --e-d-c-b-c-d-e--
    ----e-d-c-d-e----
    ------e-d-e------
    --------e--------
"""
ALPHA = {num: let for num, let in zip(range(1, 27), list(map(chr, range(97, 123))))}
FILL = '-'

def print_rangoli(size):
    # your code goes here
    width = size * 4 - 3
    rangoli_list = []
    head = []
    tail = []
    for i in range(size):
        try:
            tail.insert(0, head[-1])
        except IndexError:
            pass
        head.append(ALPHA[size - i])
        rangoli_list.append('-'.join(head + tail).center(width, FILL))
    rangoli_list += [rangoli_list[size - 2 - i] for i in range(size - 1)]
    print('\n'.join(rangoli_list))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)

