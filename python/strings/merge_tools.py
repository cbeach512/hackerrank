#!/usr/bin/env python3
"""Merge the tools!
Consider the following:
  - A string, s, of length n where s = c0 + c1 ... cn-1.
  - An integer, k, where k is a factor of n.
We can split s into n/k subsegments where each subsegment, ti, consists of a contiguous block of k characters in s. Then, use each ti to create string ui such that:
  - The characters in ui are a subsequence of the characters in ti.
  - Any repeat occurrence of a character is removed from the string such that each character in ui occurs exactly once. In other words, if the character at some index j in ti occurs at a previous index <j in ti, then do not include the character in string ui.
Given s and k, print n/k lines where each line i denotes string ui.
- Input Format
The first line contains a single string denoting s.
The second line contains an integer, k, denoting the length of each subsegment.
- Constraints
  - 1 <= n <= 10^4, where n is the length of s
  - 1 <= k <= n
  - It is guaranteed that n is a multiple of k.
- Output Format
Print n/k lines where each line i contains string ui.
- Sample Input
    AABCAAADA
    3
- Sample Output
    AB
    CA
    AD
- Explanation
String s is split into n/k = 9/3 = 3 equal parts of length k = 3. We convert each ti to ui by removing any subsequent occurrences non-distinct characters in ti:
  1 t0 = 'AAB' -> u0 = 'AB'
  2 t1 = 'CAA' -> u1 = 'CA'
  3 t2 = 'ADA' -> u2 = 'AD'
We then print each ui on a new line.
"""
def merge_the_tools(string, k):
    # your code goes here
    num_parts = len(string) // k
    t = [string[i * k:i * k + k] for i in range(num_parts)]
    u = []
    for i in t:
        part = i[0]
        for v in i[1:]:
            if v not in part:
                part += v
        u.append(part)
    for i in u:
        print(i)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)

    # comment above and uncomment this to test against the maximum len of 'string'
    #import random
    #abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    #string = ''.join([random.choices(abc)[0] for _ in range(10 ** 4 - 1)])
    #k = 3
    #merge_the_tools(string, k)

