import sys

input = sys.stdin.readline

N = int(input())

x = []
for _ in range(3):
    a = list(map(int, input().split()))
    x.append(sorted(a))

ans = N
for ind in range(3):
    cur = x[ind]
    if cur[0] == cur[1]:
        continue
    mid = sum(cur) / 2
    
    for next in range(ind + 1, 3):
        nextDot = x[next]
        nextDot[0] = abs(mid - nextDot[0])
        nextDot[1] = abs(mid - nextDot[1])
        x[next] = nextDot
    ans -= min(mid, ans - mid)
print(ans)