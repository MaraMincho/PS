import sys
import collections
import functools
input = sys.stdin.readline

N = int(input())
students = [list(map(int, input().split())) for _ in range(N ** 2)]

prev = set()
pos = {}

dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
board = [list(map(lambda _: -1, range(N))) for _ in range(N)]
visited = {}

for row in range(N) :
    for col in range(N):
        temp = 0
        for dir in dirs :
            nextRow, nextCol = row + dir[0], col + dir[1]
            if 0 <= nextRow < N and 0 <= nextCol < N :
                temp += 1
        visited[(row, col)] = temp

def find(t) :
    nextPos = []
    tPos = pos.get(t)
    if tPos == None :
        return nextPos
    row, col = tPos[0], tPos[1]
    for dir in dirs :
        nextRow, nextCol = row + dir[0], col + dir[1]
        if 0 <= nextRow < N and 0 <= nextCol < N and board[nextRow][nextCol] == -1 :
            nextPos.append((nextRow, nextCol))
    return nextPos

def addStudent(t, curPos) :
    row, col = curPos[0], curPos[1]
    board[row][col] = t
    pos[t] = curPos
    prev.add(t)
    visited[curPos] = -1
    for dir in dirs :
        nextRow, nextCol = row + dir[0], col + dir[1]
        if 0 <= nextRow < N and 0 <= nextCol < N :
            visited[(nextRow, nextCol)] -= 1

def isAvailable(v) :
    if v not in prev:
        return False
    for dir in dirs :
        nextRow, nextCol = pos[v][0] + dir[0], pos[v][1] + dir[1]
        if 0 <= nextRow < N and 0 <= nextCol < N and visited[(nextRow, nextCol)] >= 0 :
            return True
    return False

for val in students :
    student, near = val[0], val[1:]
    isPrev = list(filter(lambda x: isAvailable(x), near))
    if not isPrev :
        nextPos, _ = max(visited.items(), key= lambda x: [x[1], -x[0][0], -x[0][1]])
        addStudent(student, nextPos)
        continue

    tPos = collections.Counter(functools.reduce(lambda x, y: x + find(y), isPrev, []))
    maxKey, maxVal = max(tPos.items(), key=lambda x: (x[1], -x[0][0], -x[0][1]))

    if maxVal > 1:
        addStudent(student, maxKey)
        continue
    
    minPos, _ = min(tPos.items(), key=lambda x: (-visited[x[0]], x[0][0], x[0][1]))
    addStudent(student, minPos)



res = 0
score = {0: 0, 1: 1, 2: 10, 3: 100, 4: 1000}
for val in students :
    student, near = val[0], val[1:]
    curRow, curCol = pos[student]
    temp = 0
    for dir in dirs :
        nextRow, nextCol = curRow + dir[0], curCol + dir[1]
        if 0 <= nextRow < N and 0 <= nextCol < N and board[nextRow][nextCol] in near:
            temp += 1
    res += score[temp]
print(res)

# 5
# 1 0 0 0
# 2 0 0 0
# 3 0 0 0
# 4 0 0 0
# 5 0 0 0
# 6 0 0 0
# 7 0 0 0
# 8 0 0 0
# 9 0 0 0
# 10 0 0 0
# 11 0 0 0
# 12 0 0 0
# 13 0 0 0
# 14 0 0 0
# 15 0 0 0
# 16 0 0 0
# 17 0 0 0
# 18 0 0 0
# 19 0 0 0
# 20 0 0 0
# 21 0 0 0
# 22 0 0 0
# 23 0 0 0
# 24 0 0 0
# 25 0 0 0