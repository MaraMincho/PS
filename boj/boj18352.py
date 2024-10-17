## 첫째 줄에 도시의 개수 N,
# 도로의 개수 M,
# 거리 정보 K,
# 출발 도시의 번호 X가
# (2 ≤ N ≤ 300,000, 1 ≤ M ≤ 1,000,000, 1 ≤ K ≤ 300,000, 1 ≤ X ≤ N)

import sys 
import collections
input = sys.stdin.readline

(N, M, K, X) = list(map(int, input().split()))
graph = collections.defaultdict(list)

for _ in range(M):
    fromV, toV = list(map(int, input().split()))
    graph[fromV].append(toV)

routes = [sys.maxsize] * (N + 1)
routes[X] = 0
## [(from, to)]
q = collections.deque()
list(map(lambda x: q.append((X,x)), graph[X]))
visited = [False] * (N + 1)
while q :
    fromInd, nextInd = q.popleft()
    if visited[nextInd] :
        continue
    visited[nextInd] = True
    if routes[fromInd] + 1 < routes[nextInd]:
        routes[nextInd] = routes[fromInd] + 1
    if routes[nextInd] < K :
        list(map(lambda x: q.append((nextInd,x)), graph[nextInd]))

res = list(filter(lambda x: x[1] == K, enumerate(routes)))
res = list(map(lambda x: int(x[0]), res))
res.sort()
if res :
    print("\n".join(list(map(str, res))))
else :
    print(-1)