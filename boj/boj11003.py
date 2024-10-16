import sys
import collections

input = sys.stdin.readline

(n, m) = list(map(int, input().split()))
arrs = list(map(int, input().split()))
d = collections.deque()
d.append((arrs[0], 0))
res = [str(arrs[0])]
for ind in range(1, n):
    next = arrs[ind]
    
    while d and d[0][1] + m <= ind:
        d.popleft()
    while d and next < d[-1][0] :
        d.pop()
    d.append((next, ind))
    res.append(str(d[0][0]))
print(*res)