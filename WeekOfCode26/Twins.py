import math

def seive(n, m):
    number = [True] * (m + 1)
    number[0] = False
    number[1] = False
    prime = []
    for i in range(2, m + 1):
        if number[i]:
            j = i * 2
            while j <= m:
                number[j] = False
                j += i
    for i in range(n, m+1):
        if number[i]:
            prime.append(i)
    return prime
i = raw_input().split(" ")
n, m = int(i[0]), int(i[1])
prime = seive(0, 35000)
l = len(prime)
print l
count = 0
prime_range = []
prev = -1
curr = -1
for i in range(n, m+1):
    j = 0
    a = int(math.sqrt(i))
    print a, i
    flag = True
    while prime[j] <= a:
        if i % prime[j] == 0:
            flag = False
            break
        j += 1
    if flag:
        if curr == -1:
            curr = prev = i
        if i - prev == 2:
            count += 1
        prev = i
        prime_range.append(i)
print prime_range
print count
