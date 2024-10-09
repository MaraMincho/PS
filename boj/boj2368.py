import sys

sys.setrecursionlimit(1500000)

(maxRow, maxCol) = list(map(int, sys.stdin.readline().split()))

board = []
for _ in range(maxRow) :
    board.append(list(map(int, sys.stdin.readline().split())))

surfaces = []
steps = [(1, 0), (-1, 0), (0, 1), (0, -1)]

visited = list(map(lambda _: [False] * maxCol, range(maxRow)))
def dfs(row, col):
    global surfaces, steps, board, maxRow, maxCol, visited
    visited[row][col] = True
    for step in steps :
        nr = row + step[0]
        nc = col + step[1]
        
        if 0 <= nr < maxRow and 0 <= nc < maxCol and visited[nr][nc] == False:
            if board[nr][nc] == 0 :
                dfs(nr, nc)
            elif board[nr][nc] == 1 :
                visited[nr][nc] = True
                surfaces.append((nr, nc))

res = 0
resSurfacesCount = 0

while True :
    visited = list(map(lambda _: [False] * maxCol, range(maxRow)))
    surfaces = []
    dfs(0, 0)
    res += 1
    if surfaces == []:
        break
    for (row, col) in surfaces :
        board[row][col] = 0
    resSurfacesCount = len(surfaces)
print(res - 1)
print(resSurfacesCount)