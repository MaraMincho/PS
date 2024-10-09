
#치즈

import sys
import copy

sys.setrecursionlimit(150000)
def sol() :
    (r, c) = list(map(int, sys.stdin.readline().split()))
    board = [] 
    for _ in range(r) :
        board.append(list(map(int, sys.stdin.readline().split())))
    
    steps = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    vo = list(map(lambda x: [False] * c, range(r)))
    visited = copy.deepcopy(vo)
    s = []
    
    ### 바깥쪽 공기 
    def oDfs(row: int, col: int) :
        nonlocal r, c, board, s
        board[row][col] = -1
        for (rw, cw) in steps:
            nr = row + rw
            nc = col + cw
            
            if 0 <= nr < r and 0 <= nc < c and board[nr][nc] == 0:
                oDfs(nr, nc)
    
    ### 치즈
    def dfs(row: int, col: int) :
        nonlocal visited, r, c, board, s
        visited[row][col] = True
        for (rw, cw) in steps :
            nr = row + rw
            nc = col + cw
            if 0 <= nr < r and 0 <= nc < c and visited[nr][nc] == False and board[row][col] == 1:
                dfs(nr, nc)
        
        zc = 0
        for (rw, cw) in steps :
            nr = row + rw
            nc = col + cw
            if 0 <= nr < r and 0 <= nc < c and board[nr][nc] == -1:
                zc += 1
        if zc >= 2 :
            s.append((row, col))

    oDfs(0, 0)

    res = 0
    while True :    
        s = []
        visited = copy.deepcopy(vo)
        for rInd in range(r):
            for cInd in range(c):
                if board[rInd][cInd] == 1 and visited[rInd][cInd] == False :
                    dfs(rInd, cInd)

        for x in s :
            if board[x[0]][x[1]] == 1 :
                oDfs(x[0], x[1])
        if s == [] :
            break
        res += 1
    print(res)
sol()


# 8 9
# 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0
# 0 1 1 0 0 0 1 1 0
# 0 1 0 1 1 1 0 1 0
# 0 1 0 0 1 0 0 1 0
# 0 1 0 1 1 1 0 1 0
# 0 1 1 0 0 0 1 1 0
# 0 0 0 0 0 0 0 0 0