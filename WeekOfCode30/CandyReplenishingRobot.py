#!/bin/python
import sys

n,t = raw_input().strip().split(' ')
n,t = [int(n),int(t)]
c = map(int, raw_input().strip().split(' '))
o = n
bob = 0
for j, i in enumerate(c):
    n -= i
    if j == t-1:
        break
    if n < 5:
        bob += (o - n)
        n += (o - n)
print bob
