import sys
import copy
input = sys.stdin.readline

def spin(board) :
    spinBoard = copy.deepcopy(board)
    maxRow, maxCol = len(board), len(board[0])
    for row in range(maxRow) :
        for col in range(maxCol) :
            spinBoard[maxCol - col - 1][row] = board[row][col]
    return spinBoard

dirs = [(1, 0), (0, 1), (-1 ,0), (0, -1)]
def oneSpin(board) :
    maxRow, maxCol = len(board), len(board[0])
    spinBoard = [[-1] * maxCol for _ in range(maxRow)]
    curRow, curCol = 0, 0
    while spinBoard[curRow][curCol] == - 1:
        for dir in dirs :
            nextRow, nextCol = curRow + dir[0], curCol + dir[1]
            while 0 <= nextRow < maxRow and 0 <= nextCol < maxCol and spinBoard[nextRow][nextCol] == -1:
                spinBoard[nextRow][nextCol] = board[curRow][curCol]
                curRow, curCol = nextRow, nextCol
                nextRow, nextCol = nextRow + dir[0], nextCol + dir[1]
        curRow, curCol = curRow + 1, curCol + 1
    return spinBoard

    
def sol() :
    n, m, c = list(map(int, input().split()))
    board = [list(map(int, input().split())) for _ in range(n)]
    for _ in range(c) :
        board = oneSpin(board)
    [print(*x) for x in board]
sol()