import sys
input = sys.stdin.readline
n, m = list(map(int, input().split()))

graph = [ [sys.maxsize] * n for _ in range(n) ]
depth = [ [-1] * n for _ in range(n) ]
for _ in range(m):
    s, e, w = list(map(int, input().split()))
    s, e = s - 1, e - 1
    graph[s][e] = w
    graph[e][s] = w
    depth[s][e] = e
    depth[e][s] = s
for ind in range(n) :
    graph[ind][ind] = 0
    depth[ind][ind] = -1

for i in range(n) :
    for s in range(n):
        for e in range(n):
            if graph[s][i] + graph[i][e] < graph[s][e] :
                graph[s][e] = graph[s][i] + graph[i][e]
                depth[s][e] = depth[s][i]

for ind, val in enumerate(depth) :
    cur = list(map(lambda x: x + 1, val))
    cur[ind] = "-"
    print(*cur)