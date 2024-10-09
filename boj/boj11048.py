import sys
import collections

input = sys.stdin.readline
arrs = []
(y, x) = list(map(int, input().split()))
for _ in range(y):
    arrs.append(list(map(int, input().split())))
    
boards = [[-sys.maxsize] * x for _ in range(y)]

boards[0][0] = arrs[0][0]

q = collections.deque([(0, 0)])
dirs = [(1, 0), (0, 1)]
while q :
    curX, curY = q.popleft()
    for (dirX, dirY) in dirs :
        nextX = dirX + curX
        nextY = dirY + curY
        if 0 <= nextX < x and 0 <= nextY < y and boards[nextY][nextX] < boards[curY][curX] + arrs[nextY][nextX] :
            boards[nextY][nextX] = boards[curY][curX] + arrs[nextY][nextX]
            q.append((nextX, nextY))
print(boards[-1][-1])