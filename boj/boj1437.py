# 수분해
import math

n = int(input())
dp = [0] * (max(n + 1, 5))
dp[1] = 1
dp[2] = 2
dp[3] = 3
dp[4] = 4
if n > 3 :
    for ind in range(5, n + 1) :
        if (ind % 3 == 0) :
            dp[ind] = (dp[ind - 3] * 3) % 10007
        elif ind % 3 == 1 :
            dp[ind] = dp[ind - 3] * 3 % 10007
        else :
            dp[ind] = dp[ind - 3] * 3 % 10007
    
print(dp[n])

## 7
## 1 1 1 1 1 1 1 
## 2
## 3
## 4
## 5
## 6
## 7 7 + 1 + 1
## 8 2 2 2 + 1 
## 9 3 3 1 1 1
## 10 2 * 5
## 11 (x)
## 12 (3 + 4)

## 1, 2, 3, 4, 5, 6, 

## 8 -> 3 * 2 * 3
