import sys

n = int(sys.stdin.readline())
res = {1: 0, 0: 0, -1: 0}
def search(startRow: int, startCol: int, legnth: int) -> int :
    if legnth == 1:
        res[board[startRow][startCol]] += 1
        return

    flagValue = board[startRow][startCol]
    for rowInd in range(startRow, startRow + legnth) :
        for colInd in range(startCol, startCol + legnth ) :
            if board[rowInd][colInd] != flagValue :
                flagValue = None
    if flagValue != None :
        res[flagValue] += 1
    else :
        third = legnth // 3
        for rowInd in [startRow, startRow + third, startRow + 2 * third] :
            for colInd in [startCol, startCol + third, startCol + 2 * third] :
                search(rowInd, colInd, third)
board = []
for _ in range(n) :
    board.append(list(map(int, sys.stdin.readline().split())))
search(0, 0, n)

[print(res[x]) for x in [-1, 0, 1]]