import sys

input = sys.stdin.readline

n = int(input())
arrs = list(map(int, input().split()))
w = 1
res = 0
for cur in arrs:
    if cur == 1 :
        res += w
        w += 1
    else :
        w = 1
print(res)