import sys
input = sys.stdin.readline

def sol() :
    N, M = list(map(int, input().split()))
    board = [list(map(int, input().split())) for _ in range(N)]
    dirs = {
        1: [[(1, 0)], [(0, 1)],[(-1, 0)], [(0, -1)] ],
        2: [ [(1, 0), (-1, 0)], [(0, 1), (0, -1)]],
        3: [[(-1, 0), (0, 1)],[(0, 1), (1, 0)],[(1, 0), (0, -1)],[(0, -1), (-1, 0)]],
        4: [[(0, -1), (-1, 0), (0, 1)],[(-1, 0), (0, 1), (1, 0)],[(0, 1), (1, 0), (0, -1)],[(1, 0), (0, -1), (-1, 0)],],
        5: [[(0, 1), (1, 0), (-1, 0), (0, -1)]]
    }

    def next(row, col, dir, curVal):
        nextRow, nextCol = row + dir[0], col + dir[1]
        if 0 <= nextRow < N and 0 <= nextCol < M and board[nextRow][nextCol] != 6:
            board[nextRow][nextCol] += curVal
            next(nextRow, nextCol, dir, curVal)

    cctvs = []
    for row in range(N) :
        for col in range(M) :
            if board[row][col] != 6 and board[row][col] != 0:
                cctvs.append((row, col, board[row][col]))

    c5 = list(filter(lambda x: board[x[0]][x[1]] == 5, cctvs))
    cctvs = list(filter(lambda x: board[x[0]][x[1]] != 5, cctvs))
    for row, col, _ in c5:
        for nexts in dirs[5] :
            for nextDir in nexts :
                next(row, col, nextDir, 1)

    res = sys.maxsize
    def dfs(depth) :
        nonlocal res
        if depth == len(cctvs) :
            temp = 0
            for row in range(N):
                for col in range(M):
                    if board[row][col] == 0 :
                        temp += 1
            res = min(res, temp)
            if res == 0:
                print(0)
                exit(0)
            return

        row, col, dirInd = cctvs[depth]
        curDir = dirs[dirInd]
        for nexts in curDir:
            for nextDir in nexts:
                next(row, col, nextDir, 1)
            dfs(depth + 1)
            for nextDir in nexts:
                next(row, col, nextDir, -1)

    dfs(0)
    print(res)

sol()