import sys
import collections 
input = sys.stdin.readline


def sol() :
    L, R, C = list(map(int, input().split()))
    if L == R == C == 0:
        exit(0)
    board = []
    q = collections.deque()    
    initialFalg = False
    for ind in range(L) :
        cur = [list(map(str, input().strip())) for _ in range(R)]
        board.append(cur)
        if initialFalg == False:
            for row in range(R) :
                for col in range(C) :
                    if cur[row][col] == "S" :
                        q.append((ind, row, col, 0))
                        initialFalg = True
        input()
    visited = [ list(map(lambda x: [False] * C, range(R)))for _ in range(L)]
    dirs = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]

    while q :
        l, r, c, curTime = q.popleft()
        if board[l][r][c] == "E" :
            print(f"Escaped in {curTime} minute(s).")
            return

        for dir in dirs :
            nextL, nextR, nextC = l + dir[0], r + dir[1], c + dir[2]
            if 0 <= nextL < L and 0 <= nextR < R and 0 <= nextC < C and board[nextL][nextR][nextC] != "#" and visited[nextL][nextR][nextC] == False :
                visited[nextL][nextR][nextC] = True
                q.append((nextL, nextR, nextC, curTime + 1))
    print("Trapped!")

while True :
    sol()