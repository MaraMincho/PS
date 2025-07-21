from collections import deque
def solution(players, m, k):
    q = deque() 
    answer = 0
    curCount = 1
    for time, player in enumerate(players) :
        while q and q[0][0] + k <= time:
            curCount -= q.popleft()[1]
        
        maxCapacity = curCount * m
        if 0 <= player < maxCapacity :
            continue
    
        t = player // m + 1
        p = t - curCount
        curCount += p
        answer += p
        q.append((time, p))
    
    return answer