#!/bin/python
import sys
n = int(raw_input().strip())
a = map(int, raw_input().strip().split(' '))
# your code goes here
m = 10**9+7
a.sort()
for i in range(len(a)-1):
    b = abs(a[i]-a[i+1])
    if b < m:
        m = b
print m
