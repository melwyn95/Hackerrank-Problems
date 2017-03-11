def valid(i, j, n, m, visited):
    if i < n and i >= 0 and j < m and j >= 0 and matrix[i][j] == 1 and not visited[i][j]:
        return True
    return False
def dfs(i, j, n, m, count, visited):
    if not visited[i][j]:
        count += 1
        visited[i][j] = True
        if valid(i+1, j+1, n, m, visited):
            count = dfs(i+1, j+1, n, m, count, visited)
        if valid(i+1, j-1, n, m, visited):
            count = dfs(i+1, j-1, n, m, count, visited)
        if valid(i+1, j, n, m, visited):
            count = dfs(i+1, j, n, m, count, visited)
        if valid(i-1, j+1, n, m, visited):
            count = dfs(i-1, j+1, n, m, count, visited)
        if valid(i-1, j-1, n, m, visited):
            count = dfs(i-1, j-1, n, m, count, visited)
        if valid(i-1, j, n, m, visited):
            count = dfs(i-1, j, n, m, count, visited)
        if valid(i, j+1, n, m, visited):
            count = dfs(i, j+1, n, m, count, visited)
        if valid(i, j-1, n, m, visited):
            count = dfs(i, j-1, n, m, count, visited)
        return count
    return count
n = int(raw_input())
m = int(raw_input())

matrix = [map(int, raw_input().split()) for i in range(n)]
visited = [[False for i in range(m)] for i in range(n)]
answer = -1
for i in range(n):
    for j in range(m):
        if matrix[i][j] == 1:
            count = dfs(i, j, n, m, 0, visited)
            if count > answer:
                answer = count
print answer
