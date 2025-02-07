# import heapq
# def solution(stones, k):
#     if k == 1 :
#         return min(stones)
    
#     res = [] 
    
#     for ind in range(len(stones) - k):
#         res.append(max(stones[ind: ind + k]))
    
#     return min(res)

import collections
def solution(stones, k):
    d = collections.deque()
    res = 0
    for ind in range(len(stones)) :
        while d and d[0] + k < ind :
            d.popleft()
        
        while d and stones[ind] < stones[d[-1]] :
            d.pop()

        d.append(ind)
        
        if ind <= k - 1 :
            res = max(res, d[-1])
    return res

print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1],3))