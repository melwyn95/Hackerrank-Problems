def sol(n, x, y):
    board = [[1000000000000000000000000000000000000 for j in range(n)] for i in range(n)]
    def move(c_x, c_y, n, x, y, step):
        # print c_x, c_y
        # for row in board:
        #     print row
        if c_x >= n or c_y >= n or c_x < 0 or c_y < 0:
            return 11111
        if board[c_x][c_y] == 1000000000000000000000000000000000000:
            board[c_x][c_y] = step

            board[c_y][c_x] = step
        else:
            board[c_x][c_y] = min(step, board[c_x][c_y])

            board[c_y][c_x] = min(step, board[c_y][c_x])

            return board[c_x][c_y]
        if c_x == n-1 and c_y == n-1:
            board[c_x][c_y] = min(step, board[c_x][c_y])

            board[c_y][c_x] = min(step, board[c_y][c_x])

            return board[c_x][c_y]
        else:
            return min( move(c_x+x, c_y+y, n, x, y, step+1), move(c_x+y, c_y+x, n, x, y, step+1),
                        move(c_x-x, c_y-y, n, x, y, step+1), move(c_x-y, c_y-x, n, x, y, step+1),
                        move(c_x+x, c_y-y, n, x, y, step+1), move(c_x+y, c_y-x, n, x, y, step+1),
                        move(c_x-x, c_y+y, n, x, y, step+1), move(c_x-y, c_y+x, n, x, y, step+1)
                        )
    move(0, 0, n, x, y, 0)
    #print move(0, 0, n, x, y, 0)
    # for row in board:
    #     print row
    return min(board[n-1-x][n-1-y], board[n-1-y][n-1-x]) + 1
n = int(raw_input())
answer = [[-1 for i in range(n-1)] for j in range(n-1)]
for i in range(1, n):
    for j in range(i, n):
        a = sol(n, i, j)
        if a >= 1000000000000000000000000000000000000:
            answer[i-1][j-1] = -1
            answer[j-1][i-1] = -1
        else:
            answer[i-1][j-1] = a
            answer[j-1][i-1] = a
        #print i, j, answer[i-1][j-1]
for r in answer:
    print " ".join(map(str, r))
