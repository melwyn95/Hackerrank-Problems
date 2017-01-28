step = 0
def valid(row, col):
    return row >= 0 and row < n and col >= 0 and col < m
def multiple_paths(matrix, visited, row, col):
    paths = 0
    if valid(row-1, col) and not visited[row-1][col] and matrix[row-1][col] != 'X':
        paths += 1
    if valid(row+1, col) and not visited[row+1][col] and matrix[row+1][col] != 'X':
        paths += 1
    if valid(row, col-1) and not visited[row][col-1] and matrix[row][col-1] != 'X':
        paths += 1
    if valid(row, col+1) and not visited[row][col+1] and matrix[row][col+1] != 'X':
        paths += 1
    return paths >= 2

def multi_paths(matrix, row, col):
    paths = 0
    if valid(row-1, col) and matrix[row-1][col] != 'X':
        paths += 1
    if valid(row+1, col) and matrix[row+1][col] != 'X':
        paths += 1
    if valid(row, col-1) and matrix[row][col-1] != 'X':
        paths += 1
    if valid(row, col+1) and matrix[row][col+1] != 'X':
        paths += 1
    return paths > 2

def dfs(matrix, visited, row, col, n, m):
    #print row, col
    # boundaries
    if valid(row, col):
        if matrix[row][col] == '*':
            return True
        else:
            if visited[row][col]:
                return False
            else:
                visited[row][col] = True
                if multiple_paths(matrix, visited, row, col):
                    #print "Multiple Paths"
                    global step
                    step += 1
                up = dfs(matrix, visited, row, col-1, n, m)
                global path
                if up:
                    path.append((row, col-1))
                down = dfs(matrix, visited, row, col+1, n, m)
                if down:
                    path.append((row, col+1))
                left = dfs(matrix, visited, row-1, col, n, m)
                if left:
                    path.append((row-1, col))
                right = dfs(matrix, visited, row+1, col, n, m)
                if right:
                    path.append((row+1, col))
                return up or down or right or left

    else:
        return False

t = int(raw_input())
for _ in range(t):
    n, m = map(int, raw_input().split())
    matrix = []
    start_row = -1
    start_col = -1
    for row in range(n):
        r = list(raw_input())
        if 'M' in r:
            start_row = row
            start_col = r.index('M')
        matrix.append(r)
    k = int(raw_input())
    visited = [[col == 'X' for col in row] for row in matrix]
    #print matrix
    #print visited
    #print start_row, start_col
    #print dfs(matrix, visited, start_row, start_col, n, m)
    #print step
    a = 0
    if multiple_paths(matrix, visited, start_row, start_col):
        a += 1
    path = []
    dfs(matrix, visited, start_row, start_col, n, m)
    step = 0
    for i in path[1:]:
        if multi_paths(matrix, i[0], i[1]):
            a += 1
    if a == k:
        print "Impressed"
    else:
        print "Oops!"
