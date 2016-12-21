#!/bin/python

import sys


n,m = raw_input().strip().split(' ')
n,m = [int(n),int(m)]
print (n / 2 + n % 2) * (m / 2 + m % 2)
