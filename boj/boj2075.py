import sys
input = sys.stdin.readline
import heapq

n = int(input())
hq = []
res = -sys.maxsize

cur = list(map(int, input().split()))
[heapq.heappush(hq, cur) for cur in cur]
for _ in range(n - 1):
    cur = list(map(int, input().split()))
    for cur in cur :
        if cur > hq[0] :
            heapq.heappop(hq)
            heapq.heappush(hq, cur)
print(hq[0])