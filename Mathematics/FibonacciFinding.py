def mul(A, B):
    MOD = 10 ** 9 + 7
    return [    [   ((A[0][0]*B[0][0]) % MOD + (A[0][1]*B[1][0]) % MOD) % MOD,
                    ((A[0][0]*B[0][1]) % MOD + (A[0][1]*B[1][1]) % MOD) % MOD
                ],
                [   ((A[1][0]*B[0][0]) % MOD + (A[1][1]*B[1][0]) % MOD) % MOD,
                    ((A[1][0]*B[0][1]) % MOD + (A[1][1]*B[1][1]) % MOD) % MOD
                ]
            ]

def matrix_expo(A, n):
    if n == 1:
        return A
    elif n % 2 == 1:
        return mul(A, matrix_expo(A, n-1))
    B = matrix_expo(A, n/2)
    return mul(B, B)

MOD = 10 ** 9 + 7
t = int(raw_input())
for i in range(t):
    a, b, n = map(int, raw_input().split(" "))
    A = [[1, 1], [1, 0]]

    if n > 1:
        A = matrix_expo(A, n-1)
        print ((A[0][0] * b) % MOD + (A[0][1] * a) % MOD) % MOD
    else:
        if n == 0:
            print a % MOD
        elif n == 1:
            print b % MOD
