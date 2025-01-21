import sys
sys.setrecursionlimit(10**6)  # 재귀 깊이 제한 증가
input = sys.stdin.readline

def sol():
    N, M = map(int, input().split())
    board = [list(input().strip()) for _ in range(N)]

    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    visited = [[False] * M for _ in range(N)]  
    
    def dfs(x, y, start_x, start_y, count):
        visited[x][y] = True
        
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            
            if 0 <= nx < N and 0 <= ny < M and board[nx][ny] == board[x][y]:
                if nx == start_x and ny == start_y and count >= 4:
                    return True
                if not visited[nx][ny]:
                    if dfs(nx, ny, start_x, start_y, count + 1):
                        return True
    
        visited[x][y] = False
        return False

    for i in range(N):
        for j in range(M):
            if not visited[i][j]:
                if dfs(i, j, i, j, 1):
                    return True
    return False

print("Yes" if sol() else "No")
