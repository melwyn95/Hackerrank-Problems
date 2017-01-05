#!/bin/python

import sys
def binary_search(a, e, start, end):
    if start <= end:
        mid = (start + end) / 2
        if a[mid] == e:
            return True
        else:
            if a[mid] > e:
                return binary_search(a, e, start, mid - 1)
            else:
                return binary_search(a, e, mid + 1, end)
    return False

'''a = [1, 2, 3, 4]
for i in range(10):
    print i, binary_search(a, i, 0, 3)
'''

n,k = raw_input().strip().split(' ')
n,k = [int(n),int(k)]
x = map(int,raw_input().strip().split(' '))
x.sort()
i = 0
count = 0
while i < n:
    t = x[i] + k
    if t in x:
        count += 1
    else:
        while not binary_search(x, t, 0, n-1):#while t not in x:
            t -= 1
        count += 1
    t += k
    #print i, t
    while i < n and x[i] <= t:
        i += 1
print count 
