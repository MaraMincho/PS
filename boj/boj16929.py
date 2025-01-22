import sys
sys.setrecursionlimit(10**6)  # 재귀 깊이 제한 증가
input = sys.stdin.readline

def sol():
    N, M = list(map(int, input().split()))
    
    board = list(map(lambda _: input().strip(), range(N)))
    
    t = []
    visited = list(map(lambda _: ([False] * M)[:], range(N)))
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    def dfs(row, col, depth) :
        visited[row][col] = True
        for (wr, wc) in dirs :
            nr, nc = wr + row, col + wc
            
            if 0 <= nr < N and 0 <= nc < M and board[row][col] == board[nr][nc] :
                if nr == t[0] and nc == t[1] and depth >= 4 :
                    return True
                if visited[nr][nc] == False:
                    if dfs(nr, nc, depth + 1) :
                        return True
        visited[row][col] = False
        return False
    
    for row in range(N) :
        for col in range(M):
            t = [row, col]
            temp = dfs(row, col, 1)
            if temp :
                return True
    return False
print("Yes" if sol() else "No")