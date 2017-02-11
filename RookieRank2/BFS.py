# n = int(raw_input())
# board = [[0 for i in range(n)] for j in range(n)]
def valid(children, n):
    children_list = []
    for child in children:
        if child[0]>=0 and child[0]<n and child[1]>=0 and child[1]<n:
            children_list.append(child)
    return children_list
def genetate_children(x, y, a, b, n):
    return valid([
            (x+a, y+b), (x+a, y-b),
            (x-a, y+b), (x-a, y-b),
            (x+b, y-a), (x+b, y+a),
            (x-b, y-a), (x-b, y+a)
            ], n)
def bfs(a, b, n):
    children = genetate_children(0, 0, a, b, n)
    queue = []
    queue_counts = []
    step = 1
    for child in children:
        if board[child[0]][child[1]] == 0:
            board[child[0]][child[1]] = step
        #else:
        #    board[child[0]][child[1]] = min(step, board[child[0]][child[1]])
        c = genetate_children(child[0], child[1], a, b, n)
        for i in c:
            queue.append(i)
            queue_counts.append(1)
    # print queue
    # for row in board:
    #     print row
    while len(queue) > 0:
        # print queue
        # for row in board:
        #     print row
        # print len(queue)
        child = queue.pop(0)
        child_count = queue_counts.pop(0)
        if board[child[0]][child[1]] == 0:
            board[child[0]][child[1]] = child_count+1
        #else:
        #    board[child[0]][child[1]] = min(step, board[child[0]][child[1]])
        c = genetate_children(child[0], child[1], a, b, n)
        for i in c:
            if i not in queue and board[i[0]][i[1]] == 0:
                queue.append(i)
                queue_counts.append(child_count+1)
    return board[n-1][n-1]

n = int(raw_input())
# board = [[0 for i in range(n)] for j in range(n)]
# print bfs(1, 3, 5)


answer = [[0 for p in range(n-1)]for q in range(n-1)]
for i in range(1, n):
    for j in range(i, n):
        board = [[0 for p in range(n)] for q in range(n)]
        v = bfs(i, j, n)
        if v > 0:
            answer[i-1][j-1] = v
            answer[j-1][i-1] = v
        else:
            answer[i-1][j-1] = -1
            answer[j-1][i-1] = -1
for row in answer:
    print " ".join(map(str, row))
