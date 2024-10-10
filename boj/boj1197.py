import sys
sys.setrecursionlimit(10000000)

input = sys.stdin.readline

(V, E) = list(map(int, input().split()))

graph = []
for i in range(E): 
    (fromV, toV, w) = list(map(int, input().split()))
    cur = (fromV - 1, toV - 1, w)
    graph.append(cur)

graph = sorted(graph, key= lambda x: [x[2]])
unions = {}
for ind in range(V):
    unions[ind] = ind

res = 0

def fp(val:int) -> int:
    if val != unions[val] :
        unions[val] = fp(unions[val])
    return unions[val]

nodeCount = 0 
for (fromV, toV, w) in graph:
    fromP, toP = fp(fromV), fp(toV)
    if fromP == toP:
        continue
    res += w
    nodeCount += 1
    if nodeCount == V - 1 :
        break
    if fromP < toP :
        unions[toP] = fromP
    else :
        unions[fromP] = toP
print(res)