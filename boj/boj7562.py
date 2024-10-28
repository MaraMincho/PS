import sys
import collections
input = sys.stdin.readline

board = collections.defaultdict(lambda: -1)
board[tuple([0, 0])] = 0

q = collections.deque()
q.append((0, 0))
dirs = [(2, 1), (1, 2), (-2, 1), (-1, 2), (-2, -1), (-1, -2), (2, -1), (1, -2)]
def sol() :
    line = int(input())
    fromRow, fromCol = list(map(int, input().split()))
    toRow, toCol = list(map(int, input().split()))
    toRow, toCol = toRow - fromRow, toCol - fromCol
    
    while board[tuple([toRow, toCol])] == -1 and q :
        curRow, curCol = q.popleft()
        for dir in dirs :
            nextRow, nextCol = curRow + dir[0], curCol + dir[1]
            if board[tuple([nextRow, nextCol])] == - 1:
                board[tuple([nextRow, nextCol])] = board[tuple([curRow, curCol])] + 1
                q.append((nextRow, nextCol))
    return board[tuple([toRow, toCol])]
res = [ str(sol()) for _ in range(int(input()))]
print("\n".join(res))