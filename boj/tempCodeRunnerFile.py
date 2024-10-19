import sys
input = sys.stdin.readline
words = []

### 제출 안함 
n = int(input())
tempSet = set()
for ind in range(n):
    curInput = input().strip()
    if curInput in tempSet :
        continue
    words.append([curInput, ind])
originalWords = words[:]
words.sort()
maxCount = 0
currentPrefixInd = -1
resInd = sys.maxsize
for ind in range(n - 1) :
    n0, n0Ind, n1, n1Ind = words[ind][0], words[ind][1], words[ind + 1][0], words[ind + 1][1]
    if maxCount + 1 < len(n0) and maxCount + 1 < len(n1) and n0[:maxCount + 1] == n1[:maxCount + 1] or (n0[:maxCount] == n1[:maxCount] and min(n0Ind, n1Ind) < currentPrefixInd ) :
        tempInd = 0
        while tempInd < len(n0) and tempInd < len(n1) and n0[:tempInd + 1] == n1[:tempInd + 1] :
            tempInd += 1
        maxCount = tempInd
        currentPrefixInd = min(n0Ind, n1Ind)
        resInd = ind
taregetPrefix = words[resInd][0][:maxCount]
resFlag = 0
for (word, wordInd) in originalWords:
    if taregetPrefix == word[:maxCount] :
        print(word)
        resFlag += 1
        if resFlag == 2 :
            break
