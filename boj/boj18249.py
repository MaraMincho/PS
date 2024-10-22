import sys
input = sys.stdin.readline

row, col = list(map(int, input().split()))
board = [list(map(int, input().split())) for _ in range(row)]

sumBoard = board[:]
for rowInd in range(row) :
    for colInd in range(col) :
        tempSum = board[rowInd][colInd]
        if 0 < rowInd :
            tempSum += board[rowInd - 1][colInd]
        if 0 < colInd :
            tempSum += board[rowInd][colInd - 1]
        if 0 < rowInd and 0 < colInd :
            tempSum -= board[rowInd - 1][colInd - 1]
        sumBoard[rowInd][colInd] = tempSum

for _ in range(int(input())) :
    (startRow, startCol, endRow, endCol) = list(map(lambda x: int(x) - 1, input().split()))
    tempSum = sumBoard[endRow][endCol]
    flagCount = 0
    if startCol - 1 >= 0 :
        flagCount += 1
        tempSum -= sumBoard[endRow][startCol - 1]
    if startRow - 1 >= 0 :
        flagCount += 1
        tempSum -= sumBoard[startRow - 1][endCol]
    if flagCount == 2 :
        tempSum += sumBoard[startRow - 1][startCol - 1]
    print(tempSum)