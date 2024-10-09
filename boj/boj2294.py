import sys

input = sys.stdin.readline

(n, k) = list(map(int, input().split()))
coins = []
for _ in range(n):
    coins.append(int(input()))
dp = [sys.maxsize] * (k + 1)
dp[0] = 0

for coin in coins:
    for ind in range(k + 1):
        if ind < coin :
            continue
        if dp[ind - coin] + 1 < dp[ind] :
            dp[ind] = dp[ind - coin] + 1
print(dp[k] if dp[k] != sys.maxsize else -1)