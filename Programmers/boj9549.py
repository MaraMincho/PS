import sys
input = sys.stdin.readline

abc = "abcdefghijklmnopqrstuvwxyz"
abcDict = {}
for ind in range(len(abc)):
    abcDict[abc[ind]] = ind

def sol():
    afterString = input().strip()
    beforeString = input().strip()

    x = [0] * len(abc)
    
    for cur in beforeString:
        x[abcDict[cur]] += 1
    
    target = [0] * 26
    
    for ind in range(len(beforeString)):
        target[abcDict[afterString[ind]]] += 1
    
    currentInd = len(beforeString) - 1
    while target != x and currentInd < len(afterString):
        leftInd = currentInd - len(beforeString) + 1
        leftValue = afterString[leftInd]
        target[abcDict[leftValue]] -= 1
        currentInd += 1
        if currentInd < len(afterString):
            rightInd = currentInd
            rightValue = afterString[rightInd]
            target[abcDict[rightValue]] += 1

    return target == x


for _ in range(int(input())):
    print("YES" if sol() == True else "NO")