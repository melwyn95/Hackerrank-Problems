n = int(raw_input())
a = map(int, raw_input().split())
a_sorted = sorted(a)
out = []
for i in range(n):
    if a[i] != a_sorted[i]:
        out.append(i)

if len(out) > 2:
    lb = out[0]
    ub = out[len(out)-1]
    rev = reversed(a[lb:ub+1])
    a_new = a[0:lb] + list(rev) + a[ub+1:]
    #print a_new, a[lb:ub+1:-1]
    flag = False
    for i in range(n):
        if a_sorted[i] != a_new[i]:
            flag = True
            break
    if flag:
        print "no"
    else:
        print "yes\nreverse %d %d"%(lb+1, ub+1)
else:
    print "yes\nswap %d %d"%(out[0]+1, out[1]+1)
