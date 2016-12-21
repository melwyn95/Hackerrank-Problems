#!/bin/python
import sys

n = int(raw_input().strip())
c = map(int,raw_input().strip().split(' '))
b = [True] * n
c.sort()
answer = 0
for i in range(n-1):
    if c[i] == c[i+1] and b[i] and b[i+1]:
        b[i] = b[i+1] = False
        answer += 1
print answer
