import collections
import sys


def solution(n, roads, sources, destination):
    task = collections.deque()
    visited = list(map(lambda _: sys.maxsize, range(n + 1)))
    visited[destination] = 0
    nodes = collections.defaultdict(lambda: [])
    for (v0, v1) in roads :
        nodes[v0].append(v1)
        nodes[v1].append(v0)
    
    # set initail
    for node in nodes[destination] :
        task.append((node, 1))
        visited[node] = 1
    while task :
        nv, w = task.popleft()
        for node in nodes[nv] :
            if w + 1 < visited[node] :
                visited[node] = w + 1
                task.append((node, w + 1))
    
    return list(map(lambda x: visited[x] if not visited[x] == sys.maxsize else -1, sources))