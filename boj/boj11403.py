
import sys
n = int(sys.stdin.readline())

board = list(map(lambda x: list(map(str, sys.stdin.readline().split())), range(n)))

for t in range(n): # 거치는 점
    for row in range(n): # 시작점
        for col in range(n): # 끝점
            if board[row][t] == "1" and board[t][col] == "1" :
                board[row][col] = "1" 

list(map(lambda x: print(" ".join(x)), board))
