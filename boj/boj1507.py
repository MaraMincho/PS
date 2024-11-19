import sys
input = sys.stdin.readline

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

parents = list(map(int, range(N)))
def findParents(x):
    if x != parents[x] :
        parents[x] = findParents(parents[x])
    return parents[x]

def union(x, y) :
    xP, yP = findParents(x), findParents(y)
    if xP < yP :
        parents[y] = xP
        parents[yP] = xP
    else :
        parents[x] = yP
        parents[xP] = yP
routes = []
for row in range(N) :
    for col in range(row + 1, N) :
        routes.append((board[row][col], row, col))

routes.sort(reverse= True)
unionCount = 0
res = 0
tBoard = [list(map(lambda _: 25000, range(N))) for _ in range(N)]
for ind in range(N):
    tBoard[ind][ind] = 0

while unionCount != N - 1 :
    w, x, y = routes.pop()
    if parents[x] == parents[y] :
        continue
    union(x, y)
    tBoard[x][y] = w
    tBoard[y][x] = w
    res += w
    unionCount += 1

for i in range(N):
    for s in range(N):
        for e in range(N):
            if tBoard[s][i] + tBoard[i][e] < tBoard[s][e]:
                tBoard[s][e] = tBoard[s][i] + tBoard[i][e]
[print(*x) for x in tBoard]
for row in range(N) :
    for col in range(row + 1, N) :
        if board[row][col] < tBoard[row][col] :
            res += board[row][col]
print(res)