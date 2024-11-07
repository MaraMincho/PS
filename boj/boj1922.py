import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

graph = []
for _ in range(M):
    s, e, w = list(map(int, input().split()))
    graph.append((w, s, e))
graph.sort(reverse=True)

def findParent(cur) :
    if parents[cur] != cur :
        parents[cur] = findParent(parents[cur])
    return parents[cur]

res = 0
flagCount = N - 1
parents = list(map(lambda x: x, range(N + 1)))
while graph :
    (w, s, e) = graph.pop()
    sp, ep = findParent(s), findParent(e)
    if sp == ep :
        continue
    res += w
    flagCount -= 1
    if flagCount == 0 :
        break
    if sp < ep :
        parents[e] = sp
        parents[ep] = sp
    else :
        parents[s] = ep
        parents[sp] = ep
print(res)