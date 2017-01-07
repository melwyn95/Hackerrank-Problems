#!/bin/python

import sys


s,t = raw_input().strip().split(' ')
s,t = [int(s),int(t)]
a,b = raw_input().strip().split(' ')
a,b = [int(a),int(b)]
m,n = raw_input().strip().split(' ')
m,n = [int(m),int(n)]
apple = map(int,raw_input().strip().split(' '))
orange = map(int,raw_input().strip().split(' '))
count_apples = 0
count_oranges = 0
for i in apple:
    if (a + i) >= s and (a + i) <= t:
        count_apples += 1
for i in orange:
    if (b + i) <= t and (b + i) >= s:
        count_oranges += 1
print count_apples
print count_oranges
