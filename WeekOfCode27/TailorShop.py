import sys, math


n,p = raw_input().strip().split(' ')
n,p = [int(n),int(p)]
a = map(int,raw_input().strip().split(' '))
a = [int(math.ceil(float(i) / p)) for i in a]
a.sort()
buttons = 0
for i in range(n - 1):
    #print a[i], a[i+1]
    if a[i] == a[i+1]:
        a[i+1] += 1
        buttons += a[i]
    elif a[i+1] < a[i] and a[i-1] < a[i]:
        a[i+1] = a[i] + 1
        buttons += a[i]
    else:
        buttons += a[i]
buttons += a[n-1]
print buttons
