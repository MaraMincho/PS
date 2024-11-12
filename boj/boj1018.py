import sys
input = sys.stdin.readline

N, M = list(map(int, input().split()))

board = []
for _ in range(N):
    board.append(list(map(str, input().strip())))

res = sys.maxsize
for row in range(N) :
    for col in range(M) :
        if row + 8 <= N and col + 8 <= M :
            oddBoard = {"B": 0, "W": 0}
            evenBoard = {"B": 0, "W": 0}
            for nextRow in range(row, row + 8) :
                for nextCol in range(col, col + 8) :
                    if (nextRow + nextCol) % 2 == 0 :
                        evenBoard[board[nextRow][nextCol]] += 1
                    else :
                        oddBoard[board[nextRow][nextCol]] += 1
            curVal = min([oddBoard["B"] + evenBoard["W"], oddBoard["W"] + evenBoard["B"]]) 
            res = min(res, curVal)  
print(res)