def sol(a, n):
    l_sum = 0
    r_sum = sum(a[1:])
    for i in range(n-1):
        if l_sum == r_sum:
            return True
        else:
            l_sum += a[i]
            r_sum -= a[i+1]
    return l_sum == r_sum

t = int(raw_input())
for _ in range(t):
    n = int(raw_input())
    a = map(int, raw_input().split(" "))
    if sol(a, n):
        print "YES"
    else:
        print "NO"
