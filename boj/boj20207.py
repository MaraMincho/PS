import sys

input = sys.stdin.readline

items = []
boardMaxCount = 0
for _ in range(int(input())):
    (s, e) = list(map(int, input().split()))
    boardMaxCount = max(boardMaxCount, e)
    d = e - s + 1
    items.append([s, e, d])

items = sorted(items, key = lambda x: [x[0], x[2]])

board = [0] * (boardMaxCount + 1)

for item in items :
    (s, e, d) = item
    for ind in range(s, e + 1):
        board[ind] += 1

res = 0
tempMax = 0
tempLength = 0
for bdv in board:
    if bdv == 0:
        if tempLength != 0 :
            res += tempMax * tempLength
        tempMax = 0
        tempLength = 0
        continue
    tempLength += 1
    tempMax = max(tempMax, bdv)

res += tempMax * tempLength
print(res)