#!/bin/python

import sys


n,c,m = raw_input().strip().split(' ')
n,c,m = [int(n),int(c),int(m)]
p = map(int, raw_input().strip().split(' '))
max_trip = m * c
flag = True
for i in p :
    if i > max_trip:
        flag = False
        break
if flag:
    print "Yes"
else:
    print "No"
