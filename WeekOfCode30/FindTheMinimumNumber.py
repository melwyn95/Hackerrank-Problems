#!/bin/python
import sys
n = int(raw_input().strip())
def rec(n):
    if n == 2: return 'min(int, int)'
    else: return 'min(int, '+rec(n-1)+')'
print rec(n)
