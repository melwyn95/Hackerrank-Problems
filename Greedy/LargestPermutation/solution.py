n, k = map(int, raw_input().split())
a = map(int, raw_input().split())
b = [-1 for i in range(n+1)]
if k >= n:
    a.sort(key=lambda x:-1*x)
    for i in a:
        print i,
else:
    for i, j in enumerate(a):
        b[j] = i
    maximum = n
    l = 0
    swaps = 0
    while l < n and swaps < k:
        if a[l] != maximum:
            # print a[l], maximum, a[b[maximum]]
            b_s = b[maximum]
            t = a[l]
            a[l] = maximum
            a[b[maximum]] = t
            b[maximum] = l
            b[t] = b_s
            swaps += 1
            # print a[l], maximum, a[b[maximum]]
        l += 1
        maximum -= 1

    for i in a:
        print i, 
