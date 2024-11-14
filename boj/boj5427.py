import sys
import collections
input = sys.stdin.readline

def sol() :

    w, h = list(map(int, input().split()))
    board = [list(map(str, input().strip())) for _ in range(h)]
    q = collections.deque()

    fire = []
    for row in range(h):
        for col in range(w):
            if board[row][col] == '#' :
                continue
            elif board[row][col] == "*":
                fire.append((row, col))
            elif board[row][col] == "@":
                q.append((row, col, 0))
            
    dirs = [(1, 0), (0, -1), (-1, 0), (0, 1)]
    prevTime = 0
    board[q[0][0]][q[0][1]] = "."
    visited = {}
    def fireTime() :
        nonlocal fire
        nextFire = []
        for curFire in fire :
            for dir in dirs :
                nextRow, nextCol = curFire[0] + dir[0], curFire[1] + dir[1]
                if 0 <= nextRow < h and 0 <= nextCol < w and board[nextRow][nextCol] == ".":
                    board[nextRow][nextCol] = "*"
                    nextFire.append((nextRow, nextCol))
        fire = nextFire
    while q:
        row, col, curTime = q.popleft()
        # 시간 체크
        if curTime != prevTime :
            fireTime()
            prevTime = curTime
        # 현재 위치 불일경우
        if board[row][col] == "*":
            continue
        for dir in dirs :
            nextRow, nextCol = row + dir[0], col + dir[1]
            if nextRow < 0 or h <= nextRow or nextCol < 0 or w <= nextCol :
                return str(curTime + 1)
            elif board[nextRow][nextCol] == "." and visited.get((nextRow, nextCol)) == None:
                visited[(nextRow, nextCol)] = True
                q.append((nextRow, nextCol, curTime + 1))
    return "IMPOSSIBLE"

print("\n".join(list(map(lambda _: sol(), range(int(input()))))))