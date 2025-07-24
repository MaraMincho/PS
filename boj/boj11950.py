import sys
input = sys.stdin.readline

ans = sys.maxsize

n = list(map(int, input().split()))
n = n[0]
board = list(map(lambda x: input().strip(), range(n)))[::-1]
for red in range(1, n - 1):
    for blue in range(1, n - red):
        temp = 0
        # red
        temp += len(list(filter(lambda x: x != "R", "".join(board[:red]))))
        # blue
        temp += len(list(filter(lambda x: x != "B", "".join(board[red:red + blue]))))
        # white
        temp += len(list(filter(lambda x: x != "W", "".join(board[red + blue:]))))
        ans = min(ans, temp)
print(ans)