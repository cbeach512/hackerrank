#!/usr/bin/env python3
"""Time Delta
When users post an update on social media,such as a URL, image, status update etc., other users in their network are able to view this new post on their news feed. Users can also see exactly when the post was published, i.e, how many hours, minutes or seconds ago.
Since sometimes posts are published and viewed in different time zones, this can be confusing. You are given two timestamps of one such post that a user can see on his newsfeed in the following format:
  - Day dd Mon yyyy hh:mm:ss +xxxx
Here +xxxx represents the time zone. Your task is to print the absolute difference (in seconds) between them.
- Input Format
The first line contains T, the number of testcases.
Each testcase contains 2 lines, representing time t1 and time t2.
- Constraints
Input contains only valid timestamps
year <= 3000.
- Output Format
Print the absolute difference (t1 - t2) in seconds.
- Sample Input 0
    2
    Sun 10 May 2015 13:54:36 -0700
    Sun 10 May 2015 13:54:36 -0000
    Sat 02 May 2015 19:54:36 +0530
    Fri 01 May 2015 13:54:36 -0000
- Sample Output 0
    25200
    88200
- Explanation 0
In the first query, when we compare the time in UTC for both the time stamps, we see a difference of 7 hours. which is 7x3600 seconds or 25200 seconds.
Similarly, in the second query, time difference is 5 hours and 30 minutes for time zone adjusting for that we have a difference of 1 day and 30 minutes. Or 24x3600+30x60 => 88200
"""
from calendar import month_abbr
from datetime import timezone, timedelta, datetime
import math
import os
import random
import re
import sys


MONTHS = {m: i for i, m in enumerate(month_abbr) if i > 0}


def makeTime(ts_list):
    t_d = dict()
    t_d['d'] = int(ts_list[1])
    t_d['m'] = MONTHS[ts_list[2]]
    t_d['y'] = int(ts_list[3])
    t_d['t'] = {k: int(v) for k, v in zip(['h','m','s'], ts_list[4].split(':'))}
    if ts_list[5][0] == '-':
        t_d['o'] = {'opr': -1, 'h': int(ts_list[5][1:3]), 'm': int(ts_list[5][3:5])}
    else:
        t_d['o'] = {'opr': 1, 'h': int(ts_list[5][1:3]), 'm': int(ts_list[5][3:5])}
    z = timezone(timedelta(hours=t_d['o']['opr']*t_d['o']['h'], minutes=t_d['o']['opr']*t_d['o']['m']))
    t = datetime(t_d['y'], t_d['m'], t_d['d'], t_d['t']['h'], t_d['t']['m'], t_d['t']['s'], tzinfo=z)
    return t



# Complete the time_delta function below.
def time_delta(ts1, ts2):
    t1 = makeTime(ts1.split())
    t2 = makeTime(ts2.split())
    return str(abs(int((t1-t2).total_seconds())))


def main():
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        ts1 = input()

        ts2 = input()

        delta = time_delta(ts1, ts2)

        fptr.write(delta + '\n')

    fptr.close()



if __name__ == '__main__':
    main()

