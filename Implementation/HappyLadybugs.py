#!/bin/python

import sys


Q = int(raw_input().strip())
for a0 in xrange(Q):
    n = int(raw_input().strip())
    b = raw_input().strip()
    b_set = list(set(b))
    if "_" not in b_set:
        flag = True
        for i in b_set:
            if b.count(i) == 1:
                print "NO"
                flag = False
                break
        if flag:
            f = True
            for i in b_set:
                index = b.index(i)
                if b[index + 1] != b[index]:
                    print "NO"
                    flag = False
                    break
            if flag:
                print "YES"
    else:
        b_set.remove("_")
        flag = True
        for i in b_set:
            if b.count(i) == 1:
                print "NO"
                flag = False
                break
        if flag:
            print "YES"
