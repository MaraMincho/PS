import sys
input = sys.stdin.readline

n, m = list(map(int, input().split()))

if n == 0 :
    print(0)
    exit(0)
board = list(map(int, input().split()))
res = 0
prev = 0
for cur in board :
    if prev + cur < m :
        prev += cur
    elif prev + cur == m :
        prev = 0
        res += 1
    else :
        prev = cur
        res += 1
if prev > 0 :
    res += 1
print(res)