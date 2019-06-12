#!/usr/bin/env python3
"""DefaultDict Tutorial
The defaultdict tool is a container in the collections class of Python. It's similar to the usual dictionary (dict) container, but the only difference is that a defaultdict will have a default value if that key has not been set yet. If you didn't use a defaultdict you'd have to check to see if that key exists, and if it doesn't, set it to what you want.
- For example:
    from collections import defaultdict
    d = defaultdict(list)
    d['python'].append("awesome")
    d['something-else'].append("not relevant")
    d['python'].append("language")
    for i in d.items():
        print i
  - This prints:
    ('python', ['awesome', 'language'])
    ('something-else', ['not relevant'])
In this challenge, you will be given 2 integers, n and m. There are n words, which might repeat, in word group A. There are m words belonging to word group B. For each m words, check whether the word has appeared in group A or not. Print the indices of each occurrence of m in group A. If it does not appear, print -1.
- Constraints
1 <= n <= 10000
1 <= m <= 100
1 <= length of each word in the input <= 100
- Input Format
The first line contains integers, n and m separated by a space.
The next n lines contains the words belonging to group A.
The next m lines contains the words belonging to group B.
- Output Format
Output m lines.
The ith line should contain the 1-indexed positions of the occurrences of the ith word separated by spaces.
- Sample Input
    5 2
    a
    a
    b
    a
    b
    a
    b
- Sample Output
    1 2 4
    3 5
- Explanation
'a' appeared 3 times in positions 1, 2 and 4.
'b' appeared 2 times in positions 3 and 5.
In the sample problem, if 'c' also appeared in word group B, you would print -1.
"""
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict


def get_index(a, b):
    d = defaultdict(list)
    for word in enumerate(a):
        d[word[1]].append(word[0] + 1)
    keys = d.keys()
    for word in b:
        if word not in keys:
            d[word].append(-1)
    return [d[word] for word in b]


def main():
    n, m = map(int, input().split())
    a = [input() for _ in range(n)]
    b = [input() for _ in range(m)]
    for i in get_index(a, b):
        print(' '.join(map(str, i)))


if __name__ == '__main__':
    main()

