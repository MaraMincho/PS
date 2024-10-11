import sys

input = sys.stdin.readline

n = int(input().strip())
lines = list(map(int, input().split()))
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

for ind in range(len(lines)) :
    line = lines[ind]
    if res[-1] < line:
        res.append(line)
        continue
    targetInd = findInd(line)
    res[targetInd] = line

print(len(lines) - (len(res) - 1 ))