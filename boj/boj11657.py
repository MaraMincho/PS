import sys
input = sys.stdin.readline
N, M = list(map(int, input().split()))

board = [list(map(lambda x: sys.maxsize, range(N + 1))) for _ in range(N + 1)]

for ind in range(N + 1):
    board[ind][ind] = 0

for _ in range(M) :
    x, y, w = list(map(int, input().split()))
    board[x][y] = min(board[x][y], w)
    
for i in range(N + 1):
    for s in range(N + 1) :
        for e in range(N + 1) :
            if board[s][i] + board[i][e] < board[s][e] :
                board[s][e] = board[s][i] + board[i][e]
copiedBoard = list(map(lambda x: x[:], board))

for i in range(N + 1):
    for s in range(N + 1) :
        for e in range(N + 1) :
            if board[s][i] + board[i][e] < board[s][e] :
                print(-1)
                exit(0)

res = copiedBoard[1][2:]
for cur in res :
    print( cur if cur != sys.maxsize else -1)
    