import sys
import collections
import heapq
input = sys.stdin.readline

N = int(input())
planets = []
for ind in range(N):
    x, y, z = list(map(int, input().split()))
    planets.append((ind, x, y, z))

board = [[] for _ in range(N) ]
ps = list(map(lambda ind: sorted(planets, key= lambda x: x[ind]), range(1, 4)))
# (가중치, 시작점, 끝점)
graph = collections.defaultdict(list)

def dist(x, y) :
    return min(map(lambda ind : abs(x[ind] - y[ind]), range(1, 4)))
 
def makeRoutes(sortedP) :
    for ind in range(N - 1) :
        cost = dist(sortedP[ind], sortedP[ind + 1])
        graph[sortedP[ind + 1][0]].append((cost, sortedP[ind][0]))
        graph[sortedP[ind][0]].append((cost, sortedP[ind + 1][0]))

[makeRoutes(x) for x in ps]

task = [(0, 0)]
visited = list(map(lambda _: False, range(N)))
res = 0
flagCount = N
while task :
    w, v = heapq.heappop(task)
    if visited[v] :
        continue
    visited[v] = True
    res += w
    flagCount -= 1
    if flagCount == 0 :
        break
    for nextW, nextV in graph[v] :
        if visited[nextV] == False:
            heapq.heappush(task, (nextW, nextV))
print(res)