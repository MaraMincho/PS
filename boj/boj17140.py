import sys

(r, c, k) = list(map(int, input().split()))
tt = list(map(lambda _ : [0] * 100, range(100)))
p = [0] * 100
for row in range(3) :
    for (col, val) in enumerate(list(map(int, input().split()))):
        tt[row][col] = val

def sl(curs) :
    curDict = {}
    for cur in curs :
        curDict[cur] = curDict.get(cur, 0) + 1
    
    if curDict.get(0, None) != None :
        curDict.pop(0)
    items = list(map(lambda x: [x[0], x[1]], curDict.items()))
    sortedItems = sorted(items, key=lambda x: [x[1], x[0]])

    flatItems = sum(sortedItems, [])
    
    return flatItems[: min(len(flatItems), 100)]

curRowCount = 3
curColCount = 3
res = 0

while tt[r - 1][c - 1] != k and res <= 100:
    if curRowCount >= curColCount :
        curRowInd = 0
        while curRowInd < curRowCount :
            curVal = sl(tt[curRowInd])
            for col in range(100):
                if col < len(curVal) :
                    tt[curRowInd][col] = curVal[col]
                else :
                    tt[curRowInd][col] = 0
            curColCount = max(curColCount, len(curVal))
            curRowInd += 1
    else:
        curRowInd = 0
        while curRowInd < curColCount :

            curCol = list(map(lambda x: tt[x][curRowInd], range(curRowCount)))
            curVal = sl(curCol)
            for ind in range(100) :
                if ind < len(curVal) :
                    tt[ind][curRowInd] = curVal[ind]
                else :
                    tt[ind][curRowInd] = 0
            curRowCount = max(curRowCount, len(curVal))
            curRowInd += 1
    res += 1
print(res if res <= 100 else -1)