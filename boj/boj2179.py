import sys
input = sys.stdin.readline
words = []

### 제출 안함 
n = int(input())
[words.append(input().strip()) for _ in range(n)]
originalWords = words[:]
words.sort()

maxCount = 0
resInd = -1
for ind in range(n - 1) :
    n0, n1 = words[ind], words[ind + 1]
    
    if maxCount + 1 < len(n0) and maxCount + 1 < len(n1) and n0[:maxCount + 1] == n1[:maxCount + 1] :
        tempInd = 0
        while tempInd < len(n0) and tempInd < len(n1) and n0[:tempInd + 1] == n1[:tempInd + 1] :
            tempInd += 1
        maxCount = tempInd
        resInd = ind
taregetPrefix = words[resInd][:maxCount]
resFlag = 0
for word in originalWords:
    if taregetPrefix in word :
        print(word)
        resFlag += 1
        if resFlag == 2 :
            break

