import sys
input = sys.stdin.readline

## 양방향 통행 가능.
# 지역의 개수, 수색 범위, 길의 개수
n, m , r = list(map(int, input().split()))
values = list(map(lambda x: int(x), input().split()))
board = [[sys.maxsize for _ in range(n)] for _ in range(n)]
graph = {}
for _ in range(r):
    (fromV, toV, w) = list(map(lambda x: int(x) - 1, input().split()))
    board[fromV][toV] = w + 1
    board[toV][fromV] = w + 1
for ind in range(n):
    board[ind][ind] = 0
for interV in range(n):
    for startV in range(n):
        for endV in range(n):
            board[startV][endV] = min(board[startV][interV] + board[interV][endV], board[startV][endV])

res = 0
for ele in board:
    avaiables = list(filter(lambda x: x[1] <= m, enumerate(ele)))
    curSum = sum(list(map(lambda x: values[x[0]], avaiables)))
    res = max(res, curSum)
print(res)