import sys
from collections import deque
import copy

gears = []

leftInd = 2
rightInd = 6

def rotate(dir, d: deque) :
    if dir == 1 :
        cur = d.pop()
        d.appendleft(cur)
    else :
        cur = d.popleft()
        d.append(cur)


for _ in range(4) :
    cur = list(map(int, sys.stdin.readline().strip()))
    gears.append(deque(cur))
    
rl = []

def isDif(a, b) :
    return a[2] != b[6]

steps = [1, -1]
for _ in range(int(sys.stdin.readline())) :
    tempGears = copy.deepcopy(gears)
    (t, d) = list(map(int, sys.stdin.readline().split()))
    t -= 1
    
    dif = set()
    gearsDir = [0] * 4
    
    for ind in range(3) :
        if isDif(gears[ind], gears[ind + 1]) :
            dif.add(ind * 10 + (ind + 1))

    gearsDir[t] = d
    rotate(d, tempGears[t])
    
    curInd = t
    while curInd + 1 < 4 and curInd * 10 + (curInd + 1) in dif:
        curDir = gearsDir[curInd]
        gearsDir[curInd + 1] = -curDir
        rotate(-curDir, tempGears[curInd + 1])
        curInd += 1

    curInd = t
    while curInd - 1 >= 0 and (curInd - 1) * 10 + (curInd) in dif :
        
        curDir = gearsDir[curInd]
        gearsDir[curInd - 1] = -curDir
        rotate(-curDir, tempGears[curInd - 1])
        curInd -= 1
    gears = tempGears


print( gears[0][0] + gears[1][0] * 2 + gears[2][0] * 4 + gears[3][0] * 8)