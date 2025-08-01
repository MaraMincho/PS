import sys
input = sys.stdin.readline
N = int(input())
board = [[1, 1, 1, 1]]
for _ in range(N - 2):
    board.append(list(map(int, list(input().strip()))))
board.append([1, 1, 1, 1])

# 단순 구현, 내려가는 것으로

ansBoard = [[0, 1, 2, 3]]
for row in range(N - 2):
    nextCols = board[row + 1]
    nextColsTarget = list(filter(lambda x: x[1] == 0, enumerate(nextCols)))
    nextColsTarget = list(map(lambda x: x[0], nextColsTarget))
    nextRow = []
    for col in range(4):
        currentNextColsTarget = list(map(lambda x: abs(x - col), nextColsTarget))
        minVal = currentNextColsTarget[0]
        minVal = minVal if minVal != 3 else 1
        nextRow.append(minVal + 1 + ansBoard[row][col])
    ansBoard.append(nextRow)

t = []
for col in range(4):
    lastElement = ansBoard[-1]
    t.append(4 - (col + 1) + lastElement[col] + 1)
ansBoard.append(t)
print(min(ansBoard[-1]))