
import sys

N, M = list(map(int, sys.stdin.readline().split()))

arr = list(map(int, sys.stdin.readline().split()))

gap = []
dp = [0]
for ind in range(1, N) :
    absVal = abs(arr[ind] - arr[ind - 1])
    gap.append(absVal)
    dp.append(dp[ind - 1] + absVal)

res = []
for _ in range(M):
    (fVal, sVal) = list(map(int, sys.stdin.readline().split()))
    if not (fVal < sVal) :
        res.append("0")
        continue
    
    res.append(str(dp[sVal - 1] - dp[fVal - 1]))

print("\n".join(res))