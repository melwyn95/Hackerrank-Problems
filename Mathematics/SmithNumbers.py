import math

def seive(n):
    numbers = [True] * (n + 7)
    for i in range(2, n + 1):
        if numbers[i]:
            j = i * 2
            while j <= n:
                numbers[j] = False
                j += i
    primes = []
    for i in range(2, n):
        if numbers[i]:
            primes.append(i)
    return primes

def digit_sum(n):
    s = 0
    while n > 0:
        s += n % 10
        n /= 10
    return s

n = int(raw_input())

lhs = digit_sum(n)

divisors = []
prime_factors = seive(int(math.sqrt(n) + 1))
l = len(prime_factors)
i = 0
while n > 0 and i < l:
    if n % prime_factors[i] == 0:
        divisors.append(prime_factors[i])
        n /= prime_factors[i]
    else:
        i += 1
if n > 1:
    divisors.append(n)

rhs = 0
for i in divisors:
    rhs += digit_sum(i)

#print divisors, lhs, rhs

if lhs == rhs:
    print 1
else:
    print 0
