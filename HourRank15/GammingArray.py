#!/bin/python

import sys

g = int(raw_input().strip())
for a0 in xrange(g):
    n = int(raw_input().strip())
    a = map(int, raw_input().split(" "))
    c = 0
    k = -1
    for i in a:
        if i > k:
            c += 1
            k = i
    if c % 2 == 0:
        print "ANDY"
    else:
        print "BOB"
