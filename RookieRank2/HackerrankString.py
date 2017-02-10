#!/bin/python

import sys


q = int(raw_input().strip())
h = 'hackerrank'
for a0 in xrange(q):
    s = raw_input().strip()
    # your code goes here
    c = 0
    for i in s:
        if i == h[c]:
            c += 1
            if c == 10:
                break
    if c == 10:
        print "YES"
    else:
        print "NO"
