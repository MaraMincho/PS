import sys
import heapq
input = sys.stdin.readline

(V, E) = list(map(int, input().split()))
K = int(input())

graph = [[] for _ in range(V + 1)]
for _ in range(E):
    startV, toV, w = map(int, input().split())
    graph[startV].append((w, toV))

routes = [sys.maxsize] * (V + 1)
routes[K] = 0

hq = [(0, K)] 

while hq:
    cur_dist, cur_node = heapq.heappop(hq)

    if cur_dist > routes[cur_node]:
        continue
    
    for weight, next_node in graph[cur_node]:
        new_dist = cur_dist + weight
        if new_dist < routes[next_node]:
            routes[next_node] = new_dist
            heapq.heappush(hq, (new_dist, next_node))

for route in routes[1:]:
    if route == sys.maxsize:
        print("INF")
    else:
        print(route)
