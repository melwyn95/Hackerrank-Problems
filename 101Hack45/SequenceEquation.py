n = int(raw_input())
p = map(int, raw_input().split())
for i in range(1, n+1):
    index = p.index(i) + 1# p(p(y)) = x so.. p(y) = index
    #print i, index
    index = p.index(index)
    print index + 1
