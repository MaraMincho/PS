import sys
import collections

input = sys.stdin.readline

def sol():
    N, K = list(map(int, input().split()))
    times = list(map(int, input().split()))
    times = [0] + times[:]
    graph = collections.defaultdict(list, [])
    effect = [0] * (N + 1)
    for _ in range(K):
        (u, v) = list(map(int, input().split()))
        graph[u].append(v)
        effect[v] += 1
    q = collections.deque()
    res = [-1] * (N + 1)
    for i in range(1, N + 1):
        if effect[i] == 0 :
            q.append(i)
            res[i] = 0
    targetPoint = int(input())

    while True :
        cur = q.popleft()
        curTime = times[cur]
        res[cur] += curTime
        if cur == targetPoint:
            break
        
        for next in graph[cur] :
            effect[next] -= 1
            res[next] = max(res[cur], res[next])
            if effect[next] == 0 :
                q.append(next)

    return res[targetPoint]

res = []
for _ in range(int(input())):
    res.append(str(sol()))
print("\n".join(res))