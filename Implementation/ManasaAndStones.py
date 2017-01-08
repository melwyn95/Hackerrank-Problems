t = int(raw_input())
for _ in range(t):
    n = int(raw_input())
    a = int(raw_input())
    b = int(raw_input())
    if a > b:
        a, b = b, a
    start = a * (n-1)
    end = b * (n-1)
    diff = b - a
    answer = [start]
    #print start, end, diff
    while start < end:
        start += diff
        answer.append(start)
    #print answer
    s = ""
    for i in answer:
        s += (str(i) + " ")
    print s.strip()
