n = int(raw_input())
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
c = 0
for a in range(1, n+1):
    for b in range(a+1, n+1):
        g = gcd(a, b)
        #print a, b, g
        if n % g == 0 and (g - a) / b >= 0:
            c += 1
            print a, b
print c
