
import sys

global prims
prims = [True] * (10000 + 1)
for ind in range(2, 10000 + 1) :
    if prims[ind] == False:
        continue
    temp = ind
    while temp + ind < 10000 + 1 :
        prims[temp + ind] = False
        temp += ind

primList = []
for (ind, val) in enumerate(prims):
    if val == True :
        primList.append(ind)
primList = primList[2:]


res = []
def sol(val: int) :
    res = []
    for curVal in primList :
        if val - curVal < curVal:
            break
        if prims[val - curVal] == True :
            res = [curVal, val - curVal]
    print(res[0], res[1])
for _ in range(int(sys.stdin.readline())) :
    n = int(sys.stdin.readline())
    if n == 0 :
        break
    sol(n)
