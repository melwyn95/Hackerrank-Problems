#!/bin/python
import sys

h = map(int,raw_input().strip().split(' '))
word = raw_input().strip()
height_list = [h[ord(i) - ord('a')] for i in word]
print len(word) * max(height_list)
