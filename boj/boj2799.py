ans = [0, 0, 0, 0, 0]
import sys

input = sys.stdin.readline

row, col = list(map(int, input().split()))
tr, tc = (row + 1) + 4 * row, (col + 1) + 4 * col

board = []
for _ in range(tr):
    board.append(input().strip())
    
for i in range(row):
    wr = (1 + i) + 4 * i
    
    for j in range(col):
        wc = (1 + j) + 4 * j
        
        s = 0
        for cc in range(4):
            if board[wr + cc][wc] == ".":
                break
            s += 1
        ans[s] += 1
print(*ans)
