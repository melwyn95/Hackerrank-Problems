#!/bin/python

import sys
def digit_sum(n):
    ret = 0
    while n > 0:
        ret += n % 10
        n /= 10
    return ret

n = int(raw_input().strip())
best_digit_sum = -1
best_number = -1
for i in range(1, n+1):
    if n % i == 0:
        curr_digit_sum = digit_sum(i)
        #print i, curr_digit_sum, best_digit_sum
        if best_digit_sum < curr_digit_sum:
            best_digit_sum = curr_digit_sum
            best_number = i
        elif curr_digit_sum == best_digit_sum and i < best_number:
            best_number = i
print best_number
