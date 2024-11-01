import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
graph = [ [] for _ in range( N + 1)]
board = [[False for _ in range(N + 1)] for _ in range(N + 1)]
for ind in range(1, N + 1) :
    board[ind][ind] = True

for _ in range(M) :
    front, end = list(map(int, input().split()))
    board[front][end] = True

for interval in range(1, N + 1) :
    for start in range(1, N + 1) :
        for end in range(1, N + 1) :
            if board[start][interval] and board[interval][end] :
                board[start][end] = True

for start in range(1, N + 1) :
    for end in range(start + 1, N + 1) :
        if board[start][end] :
            board[end][start] = True
        elif board[end][start]:
            board[start][end] = True

res = list(map(lambda ind: len(list(filter(lambda x: x == False, board[ind]))) - 1,range(1, N + 1) ))
[print(x) for x in res]
