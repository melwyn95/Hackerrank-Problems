import time
n, q = map(int, raw_input().split(" "))
# Pattern of 7 : O E O E E O O

# start = time.time()
Hack = ["Y", "X", "Y", "X", "X", "Y", "Y"]
Matrix = []
for i in range(1, n + 1):
    row = []
    for j in range(1, n + 1):
        row.append(Hack[(((i * j) ** 2) % 7) - 1])
    Matrix.append(row)

# for r in Matrix:
#     print r

Matrix_90 = [[] for i in range(n)]
Matrix_180 = [[] for i in range(n)]
Matrix_270 = [[] for i in range(n)]

count_90 = 0
count_180 = 0
count_270 = 0

j = n - 1
while j >= 0:
    r = Matrix[j]
    i = 0
    for e in r:
        if Matrix[i][abs(j - (n - 1))] != e:
            count_90 += 1
        Matrix_90[i].append(e)
        i += 1
    j -= 1
#print count_90
# for r in Matrix_90:
#     print r


j = n - 1
while j >= 0:
    r = Matrix_90[j]
    i = 0
    for e in r:
        if Matrix[i][abs(j - (n - 1))] != e:
            count_180 += 1
        Matrix_180[i].append(e)
        i += 1
    j -= 1
#print count_180

j = n - 1
while j >= 0:
    r = Matrix_180[j]
    i = 0
    for e in r:
        if Matrix[i][abs(j - (n - 1))] != e:
            count_270 += 1
        Matrix_270[i].append(e)
        i += 1
    j -= 1
#print count_270

# print time.time() - start
for i in range(q):
    query = int(raw_input())
    query /= 90
    if query % 4 == 1:
        print count_90
    elif query % 4 == 2:
        print count_180
    elif query % 4 == 3:
        print count_270
    else:
        print 0
