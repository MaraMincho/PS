
import sys
def sol() :
    n = int(sys.stdin.readline())
    
    start = list(map(int, sys.stdin.readline().split()))
    con = []
    for _ in range(n):
        con.append(list(map(int, sys.stdin.readline().split())))
    end = list(map(int, sys.stdin.readline().split()))
    
    boardTarget = [start] + con + [end]
    board = list(map(lambda x: [False] * (n + 2), range(n + 2)))
    
    
    def bd(o, n) -> int :
        return abs(o[0] - n[0]) + abs(o[1] - n[1])
    
    for row in range(n + 2):
        for col in range(n + 2):
            if bd(boardTarget[row], boardTarget[col]) <= 1000 :
                board[row][col] = True
                board[col][row] = True
    
    def dfs(row) :
        nonlocal board
        for nextRow in range(n + 2):
            if board[row][nextRow] == True and board[0][nextRow] == False :
                board[0][nextRow] = True
                dfs(nextRow)
    for ind in range(n + 2) :
        if board[0][ind] == True :
            dfs(ind)
    print("happy" if board[0][n + 1] else "sad")
for _ in range(int(sys.stdin.readline())):
    sol()