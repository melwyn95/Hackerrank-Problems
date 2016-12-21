import time
n, q = map(int, raw_input().split(" "))
# Pattern of 7 : O E O E E O O

start = time.time()
Hack = ["Y", "X", "Y", "X", "X", "Y", "Y"]
Matrix = []
for i in range(1, n + 1):
    row = []
    for j in range(1, n + 1):
        row.append(Hack[(((i * j) ** 2) % 7) - 1])
    Matrix.append(row)
#print time.time() - start

Matrix_90 = [[] for i in range(n)]
Matrix_180 = [[] for i in range(n)]
Matrix_270 = [[] for i in range(n)]

count = 0
for i in range(n):
    row = Matrix[i]
    j = 0
    for e in row:
        Matrix[j].append(e)
        if e != Matrix[i][j]:
            count += 1
        j += 1

print count
