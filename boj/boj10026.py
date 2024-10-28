import sys
sys.setrecursionlimit(10_000_000)
input = sys.stdin.readline

board = [list(map(str, input().strip())) for _ in range(int(input()))]
hBoard = []
for row in board :
    hBoard.append(list(map(lambda x: "R" if x == "G" else x, row)))

dirs = [(1, 0), (0, 1), (0, -1), (-1, 0)]
def sol(board) :
    distinctArea = 0
    maxRow, maxCol = len(board), len(board[0])
    visited = [[False] * maxCol for _ in range(maxRow)]
    
    def go(curRow, curCol, curStr) :
        for dir in dirs :
            nextRow = curRow + dir[0]
            nextCol = curCol + dir[1]
            if 0 <= nextRow < maxRow and 0 <= nextCol < maxCol and visited[nextRow][nextCol] == False and curStr == board[nextRow][nextCol]:
                visited[nextRow][nextCol] = True
                go(nextRow, nextCol, curStr)
    for row in range(maxRow) :
        for col in range(maxCol) :
            if visited[row][col] :
                continue
            distinctArea += 1
            visited[row][col] = True
            go(row, col, board[row][col])
    return distinctArea
print(*[sol(board), sol(hBoard)])