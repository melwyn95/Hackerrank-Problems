import math
primes = []
MAX = 1000007
numbers = [True] * MAX
def seive(primes):
    for i in range(2, MAX):
        if numbers[i]:
            primes.append(i)
            j = i * i
            while j < MAX:
                numbers[j] = False
                j += i
    return primes
primes = seive(primes)

q = int(raw_input())
for i in range(q):
    n = int(raw_input())
    a = 1
    i = 0
    while (a * primes[i]) <= n:
        a *= primes[i]
        i += 1
    print i
