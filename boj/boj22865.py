import sys
import collections
import heapq
input = sys.stdin.readline

N = int(input())
friends = list(map(int, input().split()))
graph = collections.defaultdict(list)
for _ in range(int(input())) :
    v0, v1, w = list(map(int, input().split()))
    graph[v0].append((w, v1))
    graph[v1].append((w, v0))

def dk(cur) :
    q = [(0, cur)]
    dist = list(map(lambda x: sys.maxsize, range( N + 1)))
    dist[cur] = 0
    while q :
        w, v = heapq.heappop(q)
        if dist[v] < w :
            continue
        for nextW, nextV in graph[v] :
            if w + nextW < dist[nextV] :
                dist[nextV] = w + nextW
                heapq.heappush(q, (w + nextW, nextV))
    return dist
friendRoutes = [dk(friends[ind]) for ind in range(3)]
curResVal = -1
curResValInd = -1
for v in range(1, N + 1) :
    currentMinVal = min(list(map(lambda x: friendRoutes[x][v], range(3))))
    if currentMinVal == 0 or currentMinVal == sys.maxsize :
        continue
    if curResVal < currentMinVal :
        curResVal = currentMinVal
        curResValInd = v
print(curResValInd)