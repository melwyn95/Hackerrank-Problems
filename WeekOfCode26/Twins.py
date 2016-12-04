import math
import time
def is_prime(n):
    if n % 2 == 0 and n > 2:
        return False
    flag = True
    n_sqrt = int(math.sqrt(n)) + 1
    for i in range(2, n_sqrt):
        if n % i == 0:
            flag = False
            break
    return flag

def seive(start, end):
    number = [True] * (end - start + 1)
    index = []
    s = start
    while s <= end:
        index.append(s)
        s += 1

    end_sqrt = int(math.sqrt(end))
    lim = start + end_sqrt
    s = start
    while s <= lim:
        if number[index.index(s)] and is_prime(s):
            j = s * 2
            while j <= end:
                print index.index(j)
                number[index.index(j)] = False
                j += s
        else:
            number[index.index(s)] = False
        s += 1
    # primes = []
    # if (start & 1) == 0:
    #     if number[index.index(start)]:
    #         primes.append(number)
    #     start += 1
    # while start <= end:
    #     if number[index.index(start)]:
    #         print start, index.index(start)
    #         primes.append(start)
    #     start += 2
    # print primes, number[0:11]
    if start % 2 == 0:
        start += 1
    count = 0
    while start <= end - 2:
        if number[index.index(start)] and number[index.index(start+2)]:
            count += 1
        start += 2
    print count

def act_seive(n, m):
    number = [True] * (m + 1)
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
# s = 2 #int(raw_input())
# e = 50#int(raw_input())
i = raw_input().split(" ")
n, m = int(i[0]), int(i[1])
prime = act_seive(n, m)
l = len(prime) - 1
count = 0
for i in range(l):
    if prime[i + 1] - prime[i] == 2:
        count += 1
print count 
