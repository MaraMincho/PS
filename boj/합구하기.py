
import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
dp = list(map(lambda _: 0, range(N)))
dp[0] = arr[0]
for ind in range(1, N) :
    dp[ind] = dp[ind - 1] + arr[ind]

res = []

for _ in range(int(sys.stdin.readline())) :
    fVal, sVal = list(map(lambda x: int(x) - 1, sys.stdin.readline().split()))
    res.append(str(dp[sVal] - dp[fVal] + arr[fVal]))
print("\n".join(res))