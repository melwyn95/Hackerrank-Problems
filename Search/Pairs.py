#!/usr/bin/py
# Head ends here
def binary_search(a, start, end, x):
    #print a[start:end+1]
    if start <= end:
        mid = (start + end) / 2
        if a[mid] == x:
            return True
        else:
            if x > a[mid]:
                return binary_search(a, mid+1, end, x)
            else:
                return binary_search(a, start, mid-1, x)
    return False
def pairs(a,k):
    #a contains array of numbers and k is the value of difference
    a.sort()
    #print a
    answer = 0
    for i in a:
        x = k+i
        if binary_search(a, 0, len(a)-1, x):
            answer += 1
    return answer
# Tail starts here
if __name__ == '__main__':
    a = map(int, raw_input().strip().split(" "))
    _a_size=a[0]
    _k=a[1]
    b = map(int, raw_input().strip().split(" "))
    print pairs(b,_k)
