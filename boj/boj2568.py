import sys

input = sys.stdin.readline

n = int(input().strip())
lines = {}
for _ in range(n):
    fv, tv = map(int, input().split())
    lines[fv] = tv
res = []

def findInd(targetValue: int) -> int:
    global res
    lo = 0
    hi = len(res)
    
    while lo + 1 < hi :
        mid = (lo + hi) // 2
        if res[mid] < targetValue :
            lo = mid
        else :
            hi = mid
    return hi
        
res.append(-1)
resInds = []

sortedItems = sorted(lines.items(), key= lambda x: x[0])
for (ind, val) in sortedItems :
    line = val
    curResCount = len(res)
    if res[-1] < line:
        res.append(line)
        resInds.append(curResCount)
        continue
    targetInd = findInd(line)
    res[targetInd] = line
    resInds.append(targetInd)

pv = []
tvi = max(resInds)
for ind in range(len(resInds)) :
    curInd = len(resInds) - ind - 1
    if tvi == resInds[curInd] :
        tvi -= 1
    else :
        pv.append(sortedItems[curInd][0])
print(len(pv))
print("\n".join(map(str, pv[::-1])))