import sys
input = sys.stdin.readline

x, y = list(map(int, input().split()))
board = list(map(lambda _: list(map(int, input().split())), range(x)))

os = []
for row in range(x):
    for col in range(y):
       if board[row][col] == 1:
           if not os:
               os = [row, col]
           else :
               print(abs(os[0] - row) + abs(os[1] - col))
               sys.exit