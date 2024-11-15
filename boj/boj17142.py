import sys
import functools
import copy
input = sys.stdin.readline

N, M = list(map(int, input().split()))

virus = []
board = []
targetCount = 0
for row in range(N) :
    cur = list(map(int, input().split()))
    for col in range(N) :
        if cur[col] == 2:
            virus.append((row, col))
    board.append(cur)
flatBoard = list(functools.reduce(lambda x, y : x + y, board, []))
targetCount = len(list(filter(lambda x: x == 0, flatBoard)))
time = 0
dirs = [(1, 0), (0, -1), (0, 1), (-1, 0)]

def next(board, targetCount, virus) :
    curTime = 0
    visited = {}
    for row, col in virus :
        visited[(row, col)] = True
    while targetCount != 0 and virus :
        nextVirus = []
        for row, col in virus :
            for dir in dirs :
                nextRow, nextCol = row + dir[0], col + dir[1]
                if 0 <= nextRow < N and 0 <= nextCol < N and visited.get((nextRow, nextCol)) == None and board[nextRow][nextCol] != 1 :
                    if board[nextRow][nextCol] == 0 :
                        targetCount -= 1    
                    board[nextRow][nextCol] = 2
                    nextVirus.append((nextRow, nextCol))
                    visited[(nextRow, nextCol)] = True
        virus = nextVirus
        curTime += 1
    return curTime if targetCount == 0 else sys.maxsize
res = sys.maxsize
currentVirus = []

def dfs(depth: int, virus) :
    global targetCount, currentVirus, res
    if depth == M :
        copiedBoard = copy.deepcopy(board)
        curTargetCount = targetCount
        curVirus = currentVirus[:]
        res = min(res, next(copiedBoard, curTargetCount, curVirus))
        if res == 0 :
            print(0)
            exit(0)
        return
    virus = copy.deepcopy(virus) 
    while virus :
        curVirus = virus.pop()
        currentVirus.append(curVirus)
        dfs(depth + 1, virus)
        currentVirus.pop()
        
virus = virus[::-1]
dfs(0, virus)
print(res if res != sys.maxsize else -1)