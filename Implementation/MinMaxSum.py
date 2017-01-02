#!/bin/python
import sys

a = map(int, raw_input().strip().split(' '))
a.sort()
print (a[0]+a[1]+a[2]+a[3]), (a[4]+a[1]+a[2]+a[3])