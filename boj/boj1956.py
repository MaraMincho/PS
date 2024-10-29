import sys
input = sys.stdin.readline

V, E = list(map(int, input().split()))

board = [list(map(lambda _ : sys.maxsize, range(V + 1))) for _ in range(V + 1)]
for _ in range(E):
    fv, tv, w = list(map(int, input().split()))
    board[fv][tv] = w

for ind in range(1, V + 1):
    board[ind][ind] = 0
for mid in range(1, V + 1) :
    for start in range(1, V + 1):
        for end in range(1, V + 1) :
            if board[start][mid] + board[mid][end] < board[start][end] :
                board[start][end] = board[start][mid] + board[mid][end]

res = sys.maxsize
for start in range(1, V + 1) :
    for end in range(start + 1, V + 1) :
        res = min(res, board[start][end] + board[end][start])
print(res if res != sys.maxsize else -1)