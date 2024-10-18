import heapq
import sys
import collections
input = sys.stdin.readline

n = int(input())
m = int(input())
edges = collections.defaultdict(list)
distances = collections.defaultdict(lambda: sys.maxsize)

def distanceKey(fromV, toV):
    return str(fromV) + "-" + str(toV)
for _ in range(m):
    (fromV, toV, w) = list(map(int, input().split()))
    curKey = distanceKey(fromV= fromV, toV= toV)
    distances[distanceKey(fromV, toV)] = min(w, distances[distanceKey(fromV, toV)] )
    edges[fromV].append(toV)

targetFromV, targetToV = list(map(int, input().split()))

# 가중치, from, next
q = []
for cur in edges[targetFromV] :
    curW = distances[distanceKey(targetFromV, cur)]
    heapq.heappush(q, [curW, targetFromV, cur])

res = [sys.maxsize] * (n + 1)
res[targetFromV] = 0
visited = [[] for _ in range(n + 1)]

while q :
    w, fromV, toV = heapq.heappop(q)
    
    if res[fromV] + w < res[toV] :
        res[toV] = res[fromV] + w
        visited[toV] = visited[fromV][:] + [fromV]
        
        for nextV in edges[toV]:
            curKey = distanceKey(toV, nextV)
            nextW = distances[curKey]
            heapq.heappush(q, [nextW, toV, nextV])
visitedCities = visited[targetToV] + [targetToV]

print(res[targetToV])
print(len(visitedCities))
print(*visitedCities)
