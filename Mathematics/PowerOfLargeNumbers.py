t = int(raw_input())
for j in range(t):
    a, b = raw_input().split(" ")
    MOD = (10 ** 9) + 7
    a_int = 0
    b_int = 0
    for i in a:
        a_int = ((((a_int % MOD) * 10) % MOD) + int(i)) % MOD
    for i in b:
        b_int = ((b_int * 10) + int(i)) % (MOD - 1)

    ans = 1
    while b_int > 0:
        if (b_int & 1) == 1:
            ans = (ans * a_int) % MOD
        b_int /= 2
        a_int = (a_int * a_int) % MOD
    print ans
