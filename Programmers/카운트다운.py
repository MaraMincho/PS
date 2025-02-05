def solution(target):
    dp = list(lambda x: [], list(range(target + 1)))
    dp[0] = [0, 0]
    for ind in range(1, 20) :
        dp[ind] = [1, 1]
    curInd = 21
    for ind in range(1, 20):
        dp[ind] = [1, 1]
        tempInd = ind
        while tempInd + 50 < target :
            dp[tempInd + 50] = [dp[tempInd][0] + 1, dp[tempInd][1] + 1]
            tempInd += 50
    print(dp)    
        
    return dp[target]

solution(21)