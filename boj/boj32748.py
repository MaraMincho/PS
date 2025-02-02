import sys
input = sys.stdin.readline

rd = {}
board = list(map(int, input().split()))
for ind in range(len(board)) :
    rd[str(board[ind])] = str(ind)
fa, fb = list(map(lambda x: x, input().split()))

a = list(map(lambda x: rd[x], fa))
b = list(map(lambda x: rd[x], fb))
res = str(int("".join(a)) + int("".join(b)))
rf = list(map(lambda x: str(board[int(x)]), res))
print("".join(rf))