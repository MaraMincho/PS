import sys
input = sys.stdin.readline

N = int(input())
board = []
for ind in range(N) :
    board.append(list(map(str, input().strip())))

def sol(startRow, startCol, legnth) -> str:
    res = ""
    flagValue = board[startRow][startCol]
    breakFalg = False
    for rowInd in range(startRow, startRow + legnth) :
        for colInd in range(startCol, startCol + legnth) :
            if flagValue != board[rowInd][colInd] :
                flagValue = None
                breakFalg = True
                break
        if breakFalg :
            break
    if flagValue != None :
        return flagValue
    else :
        quarter = legnth // 2
        for rowInd in [startRow, startRow + quarter] :
            for colInd in [startCol, startCol + quarter] :
                if quarter == 1 :
                    res += board[rowInd][colInd]
                else :
                    res += sol(rowInd, colInd, quarter)
    return "(" + res + ")"
print(sol(0, 0, N))

# 8
# 00000000
# 00000000
# 00001111
# 00001111
# 00011111
# 00111111
# 00111111
# 00111111
