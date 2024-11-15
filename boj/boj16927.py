import sys
input = sys.stdin.readline

dirs = [(1, 0), (0, 1), (-1 ,0), (0, -1)]
def oneSpin(board, count) :
    maxRow, maxCol = len(board), len(board[0])
    spinBoard = [[-1] * maxCol for _ in range(maxRow)]
    curRow, curCol = 0, 0
    tempCount = 0
    while spinBoard[curRow][curCol] == - 1:
        chain = [board[curRow][curCol]]
        chainInd = [(curRow, curCol)]
        maxCount = (maxRow - tempCount * 2) * 2 + (maxCol - tempCount * 2) * 2 - 4
        for dir in dirs :
            nextRow, nextCol = curRow + dir[0], curCol + dir[1]
            while 0 <= nextRow < maxRow and 0 <= nextCol < maxCol and spinBoard[nextRow][nextCol] == -1  and len(chain) < maxCount :
                chain.append(board[nextRow][nextCol])
                chainInd.append((nextRow, nextCol))
                curRow, curCol = nextRow, nextCol
                nextRow, nextCol = nextRow + dir[0], nextCol + dir[1]
        curRow += 1
        curCount = count % maxCount
        chain = chain[-curCount:] + chain[:-curCount]
        for ind, (row, col) in enumerate(chainInd) :
            spinBoard[row][col] = chain[ind]
        tempCount += 1
    return spinBoard

    
def sol() :
    n, m, c = list(map(int, input().split()))
    board = [list(map(int, input().split())) for _ in range(n)]
    board = oneSpin(board, c)
    [print(*x) for x in board]
sol()