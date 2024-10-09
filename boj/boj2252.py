import sys
import collections

input = sys.stdin.readline

(N, M) = list(map(int, input().split()))
graph = collections.defaultdict(list, [])
effect = collections.defaultdict(list, [])
for _ in range(M):
    (small, big) = list(map(lambda x: int(x) - 1, input().split()))
    graph[big].append(small)
    effect[small].append(big)

graphCount = {}
curQ = collections.deque()
for ind in range(N):
    if not graph[ind] :
        curQ.append(ind)
    graphCount[ind] = len(graph[ind])

res = []
while curQ :
    cur = curQ.popleft()
    res.append(cur)
    for curE in effect[cur]:
        graphCount[curE] -= 1
        if graphCount[curE] == 0:
            curQ.append(curE)

print(" ".join(map(lambda x: str(x + 1), res)))