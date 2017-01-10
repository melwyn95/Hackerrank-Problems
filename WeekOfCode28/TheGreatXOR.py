limit_list = [(2 ** i) - 1 for i in range(1, 41)]

q = int(raw_input().strip())
for a0 in xrange(q):
    x = long(raw_input().strip())
    for i in range(40):
        if x <= limit_list[i]:
            print limit_list[i] - x
            break
