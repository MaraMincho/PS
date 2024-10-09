
import sys

(t, w) = list(map(int, sys.stdin.readline().split()))
## [[(curVal, rest), (curVal, rest)]]
dp = [[(0, w), (0, w)]]
for _ in range(t) :
    (fVal, fRest) = dp[-1][0]
    (sVal, sRest) = dp[-1][1]
    
    curCherry = int(sys.stdin.readline())
    if curCherry == 1 :
        curF = (fVal + 1, fRest) if fVal + 1 + fRest >= sVal + sRest - 1 else (sVal + 1, sRest - 1)
        curS = (fVal, fRest - 1) if fVal + fRest - 1 > sVal + sRest else (sVal, sRest)
    else:
        curF = (fVal, fRest) if fVal + fRest >= sVal + sRest - 1 else (sVal, sRest - 1)
        curS = (fVal + 1, fRest - 1) if fVal + fRest > sVal + sRest + 1 else (sVal + 1, sRest)
    dp.append([curF, curS])
curFSum = min(sum(list(map(int, dp[-1][0]))), t)
curSSum = min(sum(list(map(int, dp[-1][1]))), t)
print(dp)
print(max(curFSum, curSSum))