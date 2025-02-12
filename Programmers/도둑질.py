import functools
def solution(money):
    answer = 0
    dp = [[0, 0], [0, 0], [money[0], 0]]
    
    for ind in range(1, len(money) - 1) :
        t = max(dp[-3:-1], key = lambda x: x[0])[0]
        tv = max(dp[-3:-1], key = lambda x: x[1])[1]
        dp.append([t + money[ind], tv + money[ind]])
        
    tv = max(dp[-3:-1], key = lambda x: x[1])[1]
    dp.append([tv + money[-1]])
    t = list(functools.reduce(lambda x,y: x + y, dp[-3:], []))
    return max(t)