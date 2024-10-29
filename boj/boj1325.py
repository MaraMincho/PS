import sys
import collections
input = sys.stdin.readline

V, E = list(map(int, input().split()))
graph = [ [] for _ in range( V + 1)]
for _ in range(E) :
    (end, start) = list(map(int, input().split()))
    graph[start].append(end)

res = [-1]

def bfs(root) :
    q = collections.deque([root])
    tempRes = 1
    visited = [False] * (V + 1)
    visited[root] = True
    while q :
        cur = q.popleft()
        for next in graph[cur] :
            if not visited[next] :
                visited[next] = True
                tempRes += 1
                q.append(next)
    return tempRes
for ind in range(1, V + 1) :
    res.append(bfs(ind))
maxVal = max(res)
sRes = []
for ind in range(V + 1) :
    if res[ind] == maxVal :
        sRes.append(ind)
print(*sRes)