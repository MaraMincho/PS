import sys

input = sys.stdin.readline

maxValue = 100001
at = [True] * maxValue

for ind in range(2, int(maxValue ** (1/2))):
    if at[ind] == False:
        continue
    
    cur = ind * 2
    while cur < maxValue:
        at[cur] = False
        cur += ind
    
at = list(enumerate(at))
prims = []
for (ind, val) in at[2:] :
    if val :
        prims.append(ind)


def sol():
    cur = int(input())
    x = {}
    pInd = 0
    while True:
        if cur % prims[pInd] == 0:
            cur = cur // prims[pInd]
            x[prims[pInd]] = x.get(prims[pInd], 0) + 1
        else :
            pInd += 1
        if at[cur] == True:
            x[cur] = x.get(cur, 0) + 1
            break
        elif cur == 1:
            break
    return x

for _ in range(int(input())):
    y = sorted(sol().items(), key= lambda x: x[0])
    for key in y :
        print(key[0], key[1])