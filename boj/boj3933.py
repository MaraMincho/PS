import sys
input = sys.stdin.readline

dp = list(map(lambda _: [0, 0, 0, 0][:] , range(0, 2**15 + 1)))
i = 1
while i * i < (2**15):
    dp[i * i][0] = 1
    j = i * i
    while j < 2 ** 15 :
        dp[j][1] += dp[j - i * i][0]
        dp[j][2] += dp[j - i * i][1]
        dp[j][3] += dp[j - i * i][2]
        j += 1
    i += 1
    
def sol():
    cur = int(input())
    if cur == 0 :
        exit(0)
    return sum(dp[cur])

while True:
    print(sol())