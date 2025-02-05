import sys
sys.setrecursionlimit(10 ** 6)
def solution(n, s):
    def m(n, s) :
        print(n, s)
        t = s // n
        if n == 2 :
            return [t + s % n, t]
        v = s % n
        if v > 0 :
            val = m(n - 1,  s - t - 1 )
            return [t + 1] + val
        return [t] + m(n - 1, s - t)
    if s // n <= 0 :
        return [-1]
    
    return sorted(m(n, s))

import collections
def sol2(n, s) :
    t = s // n
    q = collections.deque()
    rn = s % n
    for _ in range(n):
        q.append(0)
    for _ in range(rn):
        q.append(q.popleft() + 1)
    return list(map(lambda x: x + t, q))
    
print(sol2(10, 23))
print(sum(sol2(10, 23)))