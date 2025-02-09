import collections
import sys
import heapq
def solution(n, edge):
    answer = 0
    hq = []
    graph = collections.defaultdict(list)
    for (v0, v1) in edge:
        graph[v0].append(v1)
        graph[v1].append(v0)
    
    res = list(map(lambda _: sys.maxsize, range(n + 1)))
    res[0] = -1
    res[1] = 0
    # initailize node
    hq = [(0, 1)]
    
    while hq:
        w, cur = heapq.heappop(hq)
        if res[cur] < w:
            continue
        for next in graph[cur] :
            if res[cur] + 1 < res[next] :
                res[next] = res[cur] + 1
                heapq.heappush(hq, (res[cur] + 1, next))
    resMax = max(res)
    return len(list(filter(lambda x: x == resMax, res)))