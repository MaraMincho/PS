import sys
import itertools

input = sys.stdin.readline

original = list(map(str, input().strip()))

## "(" ind 모음
lbIndsStack = []
## (lInd, rInd)
pair = []
for (ind, cur) in enumerate(original) :
    if cur == "(":
        lbIndsStack.append(ind)
    elif cur == ")":
        lInd = lbIndsStack.pop()
        pair.append((lInd, ind))
pairCount = len(pair)

res = []
for i in range(1, pairCount + 1):    
    for tpsInd in itertools.combinations(list(range(pairCount)), i):
        tps = list(map(lambda x : pair[x], tpsInd))
        ts = original[:]
        for (lInd, rInd) in tps :
            ts[lInd] = ""
            ts[rInd] = ""
        res.append("".join(ts))
res = list(set(res))
res.sort()
print("\n".join(res))