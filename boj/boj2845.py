import sys
input = sys.stdin.readline

(L, P) = list(map(int, input().split()))
board = list(map(int, input().split()))

res = []

t = L * P
for cur in board:
    res.append(cur - t)
print(*res)