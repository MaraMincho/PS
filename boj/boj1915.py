import sys
input = sys.stdin.readline

n, m = list(map(int, input().split()))

board = []

for _ in range(n) :
    board.append(list(map(int, input().strip())))
def isSquare(startRow, startCol, width) -> bool:
    if startRow + width > n or startCol + width > m :
        return False
    for rowInd in range(startRow, startRow + width) :
        for colInd in range(startCol, startCol + width) :
            if board[rowInd][colInd] == 0 :
                return False
    return True

currentMaxWidth = 1

rowInd = 0
colInd = 0
while colInd < m and rowInd < n :
    flag = False
    if board[rowInd][colInd] == 1 :
        while isSquare(rowInd, colInd, currentMaxWidth) :
            flag = True
            currentMaxWidth += 1
        if flag :
            colInd += currentMaxWidth
    else :
        colInd += 1
    if m <= colInd :
        rowInd += 1
        colInd = 0
print(currentMaxWidth - 1)