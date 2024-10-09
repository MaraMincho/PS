import collections

n = int(input())

dp = [0] * n
dp[0] = 1

copiedVal = 0
for ind in range(1, n) :
    dp[ind] = max(dp[ind - 1] + 1, dp[ind - 1] + copiedVal)
    if ind > 3 and dp[ind] <= dp[ind - 3] * 2:
        dp[ind] = dp[ind - 3] * 2
        copiedVal = dp[ind - 3]
    if ind > 4 and dp[ind] <= dp[ind - 4] * 3 :
        dp[ind] = dp[ind - 4] * 3
        copiedVal = dp[ind - 4]
    if ind > 5 and dp[ind] <= dp[ind - 5] * 4:
        dp[ind] = dp[ind - 5] * 4
        copiedVal = dp[ind - 5]

print(dp[n - 1])