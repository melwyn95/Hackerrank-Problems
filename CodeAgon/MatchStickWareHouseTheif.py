#!/bin/python

import sys


n,c = raw_input().strip().split(' ')
n,c = [int(n),int(c)]
crate = []
total_boxes= []
for crate_i in xrange(c):
    crate_temp = map(int,raw_input().strip().split(' '))
    crate.append(crate_temp)
    total_boxes.append(crate_temp[0])
if sum(total_boxes) >= n:
    crate.sort(key=lambda x:-1*x[1])
    match_sticks = 0
    index = 0
    while n > 0:
        if n-crate[index][0] < 0:
            match_sticks += (n)*crate[index][1]
            break
        else:
            match_sticks += crate[index][0]*crate[index][1]
            n -= crate[index][0]
        index += 1
    print match_sticks
else:
    match_sticks = 0
    index = 0
    while index < c:
        match_sticks += crate[index][0]*crate[index][1]
        index += 1
    print match_sticks
