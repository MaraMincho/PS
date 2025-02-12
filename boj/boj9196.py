import sys
import math
input = sys.stdin.readline
t = []
while True :
    (x, y) = list(map(int, input().split()))
    if x == y == 0 :
        break
    d = x * x + y * y
    t.append((x, y, d))

t = sorted(t, key=lambda x: [x[2], x[1]], reverse=True)
print(t)

