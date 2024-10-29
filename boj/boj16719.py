import sys
input = sys.stdin.readline

targetString = input().strip()

targetList = []
for ind in range(len(targetString)) :
    targetChar = targetString[ind]
    targetList.append((ind, targetChar))

targetList = sorted(targetList, key= lambda x: [x[1], x[0]], reverse= True)
visited = [False] * (len(targetString))

res = []
def appendRes(curInd) :
    visited[curInd] = True
    curStr = ""
    for ind in range(len(visited)) :
        if visited[ind] == True :
            curStr += targetString[ind]
    res.append(curStr)

def cal(targetList: list):
    leftOver = []
    initialInd = targetList[-1][0]
    curStack = []
    actionStack = []
    while targetList :
        curInd, curVal = targetList.pop()
        if curStack and curInd < curStack[-1] :
            if curInd < initialInd :
                leftOver.append((curInd, curVal))
            continue
        curStack.append(curInd)
        if len(curStack) >=2 and curStack[-1] - curStack[-2] > 1 :
            actionStack.append((curStack[-2], curStack[-1]))
        appendRes(curInd)
    actionStack = actionStack[::-1]
    for start, end in actionStack :
        start, end = start + 1, end - 1
        if start == end :
            appendRes(start)
            continue
        nextCalList = []
        for nextCalInd in range(start, end + 1) :
            nextCalList.append((nextCalInd, targetString[nextCalInd]))
        nextCalList.sort(key=lambda x: [x[1], x[0]], reverse= True)
        cal(nextCalList)
    if leftOver :
        cal(leftOver[::-1])

print("\n".join(res))