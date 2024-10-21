import sys

input = sys.stdin.readline

n, m = list(map(int, input().split()))

board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

## 플로이드 워셜
for mid in range(n):
    for startV in range(n):
        for endV in range(n):
            targetW = board[startV][mid] + board[mid][endV]
            if targetW < board[startV][endV] :
                board[startV][endV] = targetW

resStr = ["Enjoy other party", "Stay here"]
res = []
for _ in range(m):
    (startV, toV, w) = list(map(int, input().split()))
    startV, toV = startV - 1, toV - 1
    res.append(resStr[0] if board[startV][toV] <= w else resStr[1])
print("\n".join(res))