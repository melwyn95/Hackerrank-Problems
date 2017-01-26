#!/bin/python

import sys


xTreasure,yTreasure = raw_input().strip().split(' ')
xTreasure,yTreasure = [long(xTreasure),long(yTreasure)]
n = int(raw_input().strip())
direction = []
for direction_i in xrange(n):
    x, y = map(long,raw_input().strip().split(' '))
    xTreasure -= x
    yTreasure -= y
# your code goes here
print xTreasure, yTreasure
