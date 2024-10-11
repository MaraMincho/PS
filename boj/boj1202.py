import sys
from functools import cmp_to_key

input = sys.stdin.readline

(N, K) = map(int, input().split())

packages = []
for _ in range(N):
    packages.append(list(map(int, input().split())))

backPacks = [-1]
for _ in range(K):
    backPacks.append(int(input()))

packages.sort(key= lambda x: [x[1], x[0]], reverse= True)
backPacks.sort()
def bs(targetVal: int):
    global backPacks
    lo, hi = 0, len(backPacks)
    
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if backPacks[mid] < targetVal :
            lo = mid
        else :
            hi = mid
    return hi
res = 0
for (curWeight, curValue) in packages :
    if backPacks[-1] < curWeight :
        continue
    res += curValue
    removeInd = bs(curWeight)
    backPacks.pop(removeInd)
    if backPacks[-1] == -1 :
        break
print(res)