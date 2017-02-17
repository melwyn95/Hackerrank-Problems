#!/bin/python

import sys


n = int(raw_input().strip())
score = map(int, raw_input().strip().split(' '))
most = score[0]
least = score[0]
count_most = 0
count_least = 0
for i in score[1:]:
    if i > most:
        most = i
        count_most += 1
    elif i < least:
        least = i
        count_least += 1
print count_most, count_least
