import sys
import collections
input = sys.stdin.readline

def sol() :
    dirs = collections.deque([(1, 0), (0, 1), (-1, 0), (0, -1)])
    
    routes = input().strip()
    visited = [(0, 0)]
    cur = (0, 0)
    for route in routes :
        if route in ["F", "B"] :
            curDir = dirs[0]
            next = (cur[0] + curDir[0], cur[1] + curDir[1])  if route == "F" else (cur[0] - curDir[0], cur[1] - curDir[1])
            visited.append(next)
            cur = next
        if route in ["L","R"] :
            if route == "L" :
                curDir = dirs.popleft()
                dirs.append(curDir)
            else :
                curDir = dirs.pop()
                dirs.appendleft(curDir)
    widthList = list(map(lambda x: x[0], visited))
    heightList = list(map(lambda x: x[1], visited))
    width = max(widthList) - min(widthList)
    height = max(heightList) - min(heightList)
    print(width * height)
for _ in range(int(input())) :
    sol()