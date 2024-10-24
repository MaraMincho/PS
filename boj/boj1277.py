import sys
import collections
import heapq
input = sys.stdin.readline

(N, W) = list(map(int, input().split()))
M = float(input())

voltexs = [-1]

def distance(f, t) -> float:
    w = (f[0] - t[0])
    h = (f[1] - t[1])
    return (w ** 2 + h ** 2) ** (1/2)

hq = []

for _ in range(N):
    voltexs.append(tuple(map(int, input().split())))

## (w, ind)
graph = collections.defaultdict(list)
for _ in range(W):
    startV, endV = list(map(int, input().split()))
    graph[startV].append((0, endV))
    graph[endV].append((0, startV))

for startInd in range(N):
    for endInd in range(startInd + 1, N):
        startV, endV = voltexs[startInd + 1], voltexs[endInd + 1]
        curDistance = distance(startV, endV)
        if curDistance <= M :
            graph[startInd + 1].append((curDistance, endInd + 1))
            graph[endInd + 1].append((curDistance, startInd + 1))
hq = [(0, 1)]
routes = [sys.maxsize] * (N + 1)
routes[1] = 0

while hq :
    w, vInd = heapq.heappop(hq)
    if routes[vInd] < w :
        continue
    for nextW, nextVInd in graph[vInd] :
        if nextW + w < routes[nextVInd] :
            routes[nextVInd] = nextW + w
            heapq.heappush(hq, (nextW + w, nextVInd))

print(int(routes[-1] * 1000))
