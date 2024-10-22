import sys
import collections
import heapq

input = sys.stdin.readline
(V, E) = list(map(int, input().split()))
T = int(input())
edges = [[] for _ in range(V + 1)]

for _ in range(E) :
    (startV, endV, w) = list(map(int, input().split()))
    edges[startV].append((w, endV))
    
routes = [sys.maxsize for _ in range(V + 1)]
routes[T] = 0
hq = [(0, T)]

while hq :
    (curW, endV) = heapq.heappop(hq)
    if routes[endV] < curW :
        continue
    for (nextW, next) in edges[endV]:
        if nextW + curW  < routes[next]:
            routes[next] = nextW + curW
            heapq.heappush(hq, (nextW + curW, next))
for cur in routes[1:]:
    print(cur if cur != sys.maxsize else "INF")