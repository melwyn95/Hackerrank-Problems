n, k = map(int, raw_input().split())
a = []
for i in range(n):
    a.append(tuple(map(int, raw_input().split())))
a.sort(key=lambda x : -1 * x[0])
a.sort(key=lambda x : -1 * x[1])
answer = 0
for i in a:
    if k > 0 and i[1] == 1:
        answer += i[0]
        k -= 1
    elif k == 0 and i[1] == 1:
        answer -= i[0]
    elif i[1] == 0:
        answer += i[0]
print answer
