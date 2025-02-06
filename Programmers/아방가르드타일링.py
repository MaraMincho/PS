def solution(n):
    dp = [(1, 0, 0), (1, 2, 0), (3, 2, 5 )]
    ind = len(dp) - 1
    s = 1000000007
    while ind < n :
        v0 = sum(dp[ind])
        v1 = sum(dp[ind - 1]) * 2
        v2 = sum(dp[ind - 2]) * 5
        dp.append((v0 % s, v1 % s, v2 % s))
        ind += 1
    print(dp)
    return sum(dp[n - 1])
# [(1, 0, 0), (1, 2, 0), (3, 2, 5), (10, 6, 5), (21, 6, 20), (47, 18, 60)]
solution(5)