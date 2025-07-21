import sys

input = sys.stdin.readline
n = int(input())
board = list(map(int, input().split()))

if n == 1:
    print(1)
    sys.exit()
# 두번의 완전 탐색을 통해서 증가하는 부분과 감소하는 부분을 찾을 예정임

start = 0
u, d = {}, {}
for ind in range(1, n):
    if board[ind] <= board[ind - 1]:
        u[start] = ind - 1
        start = ind
u[start] = ind

start = 0
for ind in range(1, n):
    if board[ind] >= board[ind - 1]:
        d[start] = ind - 1
        start = ind
d[start] = ind

answer = 0
for (key, value) in u.items():
    if d.get(value):
        answer = max(d[value] - key, answer)
print(answer + 1)