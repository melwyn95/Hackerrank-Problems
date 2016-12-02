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

s = 999000000 #int(raw_input())
e = 1000000000#int(raw_input())
seive(s, e)
