
import sys
x = int(sys.stdin.readline())
board = []
for _ in range(x):
    board.append(list(map(lambda x: x, sys.stdin.readline())))

steps = [[1, 0], [-1, 0], [0, 1], [0, -1]]

def dfs(row, col, step, cur) -> int :
    global board, x
    nr, nc = row + step[0], col + step[1]
    if 0 <= nr < x and 0 <= nc < x and board[nr][nc] == board[row][col] :
        return dfs(nr, nc, step, cur + 1)
    return cur 

dfsSteps = [[1, 0, -1, 0], [0, 1, 0, -1]]

res = 0
for row in range(x):
    for col in range(x):
        for step in steps:
            nr = row + step[0]
            nc = col + step[1]
            for dStep in dfsSteps :
                val = dfs(row, col, dStep[:2], 1) + dfs(row, col, dStep[2:], 1) - 1
                res = max(res, val)
            if 0 <= nr < x and 0 <= nc < x and board[nr][nc] != board[row][col] :
                ##swap
                board[nr][nc], board[row][col] = board[row][col], board[nr][nc]
                for dStep in dfsSteps :
                    val = dfs(row, col, dStep[:2], 1) + dfs(row, col, dStep[2:], 1) - 1
                    res = max(res, val)
                ##swap
                board[nr][nc], board[row][col] = board[row][col], board[nr][nc]
print(res)