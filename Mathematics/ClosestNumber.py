import math
def fast_power(a, x):
    if x == 0:
        return 1
    elif x % 2 == 1:
        return a * fast_power(a, x-1)
    else:
        t = fast_power(a, x/2)
        return t * t
t = int(raw_input())
for i in range(t):
    a, b, x = map(int, raw_input().split(" "))
    if b < 0:
        if a != 1:
            print 0
        else:
            print (1 / x) * x
    else:
        power = fast_power(a, b)
        first = int(math.ceil(float(power) / x)) * x
        second = (power / x) * x
        if abs(first - power) > abs(second - power):
            print second
        else:
            print first
        
