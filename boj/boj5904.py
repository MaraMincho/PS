import sys

input = sys.stdin.readline

sCache = {3: 3}
t = int(input())
cur = 3
prev = 3

while cur < t :
    prev += 1
    cur = cur + (prev) + cur
    
def dfs(cur, depth) :
    if cur == 3 :
        return 3 + depth
    next = dfs(cur - 1, depth)
    
    return next +  next