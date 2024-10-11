import sys

input = sys.stdin.readline
(N, M) = map(int, input().split())

graph = []
for _ in range(M):
    (f, t, w) = map(int, input().split())
    graph.append((f - 1, t - 1, w))
graph = sorted(graph, key= lambda x: [x[2], x[0], x[1]])

unions = [ i for i in range(N)]

def findParent(val: int)-> int:
    if val != unions[val] :
        return findParent(unions[val])
    return val
res = 0
lsatW = -1
check = 0
for (f, t, w) in graph :
    fp, tp = findParent(f), findParent(t)
    if fp == tp :
        continue
    
    lsatW = w
    res += w
    check += 1
    if check == N :
        break
    if fp < tp :
        unions[t] = fp
        unions[tp] = fp
    else :
        unions[f] = tp
        unions[fp] = tp
print(res - lsatW)