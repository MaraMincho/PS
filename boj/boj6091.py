import sys
import collections
input = sys.stdin.readline

N = int(input())

q = []
for ind in range(N - 1):
    curInput = list(map(int, input().split()))
    for nextInd in range(len(curInput)) :
        ele = (curInput[nextInd], ind, nextInd + ind + 1)
        q.append(ele)

q = sorted(q, reverse=True)
flagCount = N - 1

parents = list(range(N))
def findParent(cur) :
    if cur != parents[cur]:
        parents[cur] = findParent(parents[cur])
    return parents[cur]

def union(x, y) :
    px, py = findParent(x), findParent(y)
    if px < py :
        parents[y] = px
        parents[py] = px
    elif py < px :
        parents[x] = py
        parents[px] = py

res = collections.defaultdict(list)
while q :
    w, s, e = q.pop()
    if findParent(s) == findParent(e) :
        continue
    res[s].append(e)
    res[e].append(s)
    flagCount -= 1
    if flagCount == 0 :
        break
    union(s, e)

for _, item in sorted(res.items(), key= lambda x: x[0]) :
    item.sort()
    print(len(item), *list(map(lambda x: x + 1, item)))
