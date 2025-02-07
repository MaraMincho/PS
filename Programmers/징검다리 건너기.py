def solution(stones, k):
    if k == 1 :
        return min(stones)
    
    res = [] 
    
    for ind in range(len(stones) - k):
        res.append(max(stones[ind: ind + k]))
    
    return min(res)

import collections

def solution(stones, k):
    if len(stones) == k:
        return sum(stones)
    d = collections.deque()
    res = 10000000000000
    for ind in range(len(stones)) :
        while d and d[0] + k <= ind :
            d.popleft()
        
        while d and stones[d[-1]] < stones[ind]:
            d.pop()
    
        d.append(ind)
        if ind >= k - 1 :
            res = min(res, stones[d[0]])
    return res