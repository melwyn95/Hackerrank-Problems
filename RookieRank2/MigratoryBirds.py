#!/bin/python
import sys
n = int(raw_input().strip())
types = map(int, raw_input().strip().split(' '))
types_set = list(set(types))
count = []
for t in types_set:
    count.append(types.count(t))
max_count = max(count)
index = count.index(max_count)
print types_set[index]
