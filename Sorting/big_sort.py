#!/bin/python

import sys

def merge_sort(arr, lo, hi, n):
    if lo < hi:
        mid = (lo + hi) / 2
        arr1 = merge_sort(arr, lo, mid, n)
        arr2 = merge_sort(arr, mid+1, hi, n)
        arr3 = merge(arr1, arr2)
        return arr3
    elif lo == hi:
        return [arr[lo]]
def merge(arr1, arr2):
    arr3 = []
    i = j = 0
    l1 = len(arr1)
    l2 = len(arr2)
    while i < l1 and j < l2:
        if compare(arr1[i], arr2[j]):
            arr3.append(arr1[i])
            i += 1
        else:
            arr3.append(arr2[j])
            j += 1
    while i < l1:
        arr3.append(arr1[i])
        i += 1
    while j < l2:
        arr3.append(arr2[j])
        j += 1
    return arr3
def str_to_int(s):
    return ord(s) - ord('0')
def compare(n1, n2):
    l1 = len(n1)
    l2 = len(n2)
    if l1 < l2:
        return True
    elif l1 > l2:
        return False
    else:
        for i in range(l1):
            a = str_to_int(n1[i])
            b = str_to_int(n2[i])
            if a > b: return False
            elif a < b: return True
def bigSorting(arr):
    return merge_sort(arr, 0, len(arr)-1, len(arr))

if __name__ == "__main__":
    n = int(raw_input().strip())
    arr = []
    arr_i = 0
    for arr_i in xrange(n):
        arr_t = str(raw_input().strip())
        arr.append(arr_t)
    result = bigSorting(arr)
    print "\n".join(map(str, result))






##def merge_sort(arr, lo, hi, n):
##    if lo < hi:
##        mid = (lo + hi) / 2
##        arr1 = merge_sort(arr, lo, mid, n)
##        arr2 = merge_sort(arr, mid+1, hi, n)
##        arr3 = merge(arr1, arr2)
##        return arr3
##    elif lo == hi:
##        return [arr[lo]]
##def merge(arr1, arr2):
##    arr3 = []
##    i = j = 0
##    while i < len(arr1) and j < len(arr2):
##        if compare(arr1[i], arr2[j]):
##            arr3.append(arr1[i])
##            i += 1
##        else:
##            arr3.append(arr2[j])
##            j += 1
##    while i < len(arr1):
##        arr3.append(arr1[i])
##        i += 1
##    while j < len(arr2):
##        arr3.append(arr2[j])
##        j += 1
##    return arr3
##def str_to_int(s):
##    return ord(s) - ord('0')
##def compare(n1, n2):
##    if len(n1) < len(n2):
##        return True
##    elif len(n1) > len(n2):
##        return False
##    else:
##        for i in range(len(n1)):
##            if str_to_int(n1[i]) > str_to_int(n2[i]):
##                return False
##        return True
##
##print merge_sort(['5', '4', '3', '2', '1'], 0, 4, 5)
