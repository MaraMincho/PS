import sys
(n, k) = list(map(int, sys.stdin.readline().split()))

board = list(map(lambda x: [0] * n, range(n)))

for _ in range(k):
    (x, y) = list(map(lambda x: int(x) - 1, sys.stdin.readline().split()))
    board[y][x] = 1

for mid in range(n):
    for s in range(n):
        for e in range(n):
            if s == e :
                continue
            if board[s][mid] == -1 and board[mid][e] == -1 :
                board[s][e] = -1
                board[e][s] = 1
res = []
for _ in range(int(sys.stdin.readline())) :
    (x, y) = list(map(lambda x : int(x) - 1, sys.stdin.readline().split()))
    res.append(str(board[x][y]))

print("\n".join(res))