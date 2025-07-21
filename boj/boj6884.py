import sys
import math

input = sys.stdin.readline
t = int(input())


pBoard = []
def fillPBoard(mVal):
    global pBoard
    pBoard = list(map(lambda _: True, range(mVal + 1)))
    pBoard[0] = pBoard[1] = False
    
    for ind in range(2, math.isqrt(mVal) + 1):
        if pBoard[ind] == False:
            continue
        
        temp = ind
        while temp + ind <= mVal:
            pBoard[temp + ind] = False
            temp += ind
    
    

def sol(board):
    res = []
    
    sBoard = board[:]
    for ind in range(1, len(sBoard)):
        sBoard[ind] = sBoard[ind - 1] + sBoard[ind]

    for s in range(len(board) - 1):
        for e in range(s + 1, len(board)):
            cur = sBoard[e] - sBoard[s] + board[s]
            if pBoard[cur]:
                if not res or res[1] - res[0] > e - s:
                    res = [s, e]
    if not res:
        print("This sequence is anti-primed.")
    else:
        print(f'Shortest primed subsequence is length {res[1] - res[0] + 1}: ', end="")
        print(*board[res[0]: res[1] + 1])

boards = []
m = []
for _ in range(t):
    boards.append(list(map(int, input().split()))[1:])
    m.append(sum(boards[-1]))
fillPBoard(max(m))

for board in boards:
    sol(board=board)