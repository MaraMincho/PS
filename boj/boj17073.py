import sys
import collections
sys.setrecursionlimit(100_000_000)
input = sys.stdin.readline

N, W = list(map(int, input().split()))
graph = collections.defaultdict(list)
for _ in range(N - 1) :
    (t1v, t2v) = list(map(int, input().split()))
    graph[t1v].append(t2v)
    graph[t2v].append(t1v)

visited = collections.defaultdict(lambda: False)
res = 0
def go(root: int) :
    global visited, graph, res
    nexts = list(filter(lambda x: visited[x] == False, graph[root]))
    if len(nexts) == 0 :
        res += 1
        return
    for next in nexts:
        if visited[next] == True :
            continue
        visited[next] = True
        go(next)
visited[1] = True
go(1)
print(W / res)