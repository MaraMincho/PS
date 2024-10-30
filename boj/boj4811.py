import sys
dp = [[1], [1, 1], [2, 2, 1], [5, 5, 3, 1], [14, 14, 9, 4, 1]]

def addDP() :
    lastDP = dp[-1]
    currentSum = sum(lastDP)
    next = [currentSum, currentSum]
    prev = currentSum
    for ind in range(0, len(lastDP) - 1) :
        cur = prev - lastDP[ind]
        next.append(cur)
        prev = cur
    dp.append(next)

while True :
    t = int(input())
    if t == 0 :
        break
    while len(dp) < t :
        addDP()
    print(sum(dp[t - 1]))