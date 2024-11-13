import sys

input = sys.stdin.readline

N = int(input())
students = [list(map(int, input().split())) for _ in range(N ** 2)]

prev = set()
pos = {}

dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
board = [list(map(lambda _: -1, range(N))) for _ in range(N)]
dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
for val in students :
    student, near = val[0], val[1:]
    
    nexts = []
    for row in range(N) :
        for col in range(N):
            if board[row][col] != -1 :
                continue
            # 좋아하는사람, 공실
            f, v = 0, 0
            for dir in dirs :
                nextRow, nextCol = row + dir[0], col + dir[1]
                if 0 <= nextRow < N and 0 <= nextCol < N :
                    if board[nextRow][nextCol] == -1:
                        v += 1
                    elif board[nextRow][nextCol] in near :
                        f += 1
            cur = (f, v, row, col)
            nexts.append(cur)
    next = max(nexts, key= lambda x: [x[0], x[1], -x[2], -x[3]])
    board[next[2]][next[3]] = student
    pos[student] = (next[2], next[3])
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