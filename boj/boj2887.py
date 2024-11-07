import sys
import heapq
input = sys.stdin.readline

N = int(input())
planets = []
for ind in range(N):
    x, y, z = list(map(int, input().split()))
    planets.append((ind, x, y, z))

board = [[] for _ in range(N) ]

ps = list(map(lambda ind: sorted(planets, key= lambda x: x[ind]), range(1, 4)))
q = []
def dist(x, y) :
    currentDist = list(map(lambda ind: abs(x[ind] - y[ind]), range(1, 4)))
    return min(currentDist)

def addBoard(p) :
    for ind in range(len(p)) :
        (pInd, _, _, _) = p[ind]
        if ind > 0 :
            prevInd = p[ind - 1][0]
            curDist = dist(planets[pInd], planets[prevInd])
            nexts = prevInd, pInd if prevInd < pInd else prevInd, pInd
            q.append((curDist, nexts[0], nexts[1]))
        if ind < N - 1 :
            nextInd = p[ind + 1][0]
            curDist = dist(planets[pInd], planets[nextInd])
            nexts = nextInd, pInd if nextInd < pInd else nextInd, pInd
            q.append((curDist, nexts[0], nexts[1]))

[addBoard(x) for x in ps]

parents = list(range(N))

def find(x) :
    if parents[x] != x :
        parents[x] = find(parents[x])
    return parents[x]

def union(x, y) :
    xP, yP = find(x) , find(y)
    if xP < yP :
        parents[y] = xP
        parents[yP] = xP
    elif yP < xP :
        parents[x] = yP
        parents[xP] = yP
q = list(set(q))
q.sort()
flagCount = N - 1
res = 0

for w, s, e in q :
    if find(s) != find(e) :
        union(s, e)
        flagCount -= 1
        res += w
        if flagCount == 0 :
            break
print(res)
