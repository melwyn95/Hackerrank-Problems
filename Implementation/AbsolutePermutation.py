#!/bin/python

import sys


t = int(raw_input().strip())
for a0 in xrange(t):
    n,k = raw_input().strip().split(' ')
    n,k = [int(n),int(k)]
    final = [0 for i in range(n)]
    flag = True
    for i in range(1, n+1):
        a = i + k
        b = i - k
        if b > 0 and final[b-1] == 0:
            final[b-1] = i
        elif a <= n and final[a-1] == 0:
            final[a-1] = i
        else:
            print -1
            flag = False
            break
        #print final
    if flag:
        print " ".join(map(str, final))
