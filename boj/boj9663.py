import sys
import collections
input = sys.stdin.readline

def sol() :
    N = int(input())
    
    colVisited = collections.defaultdict(bool)
    leftVisited = collections.defaultdict(bool)
    rightVisited = collections.defaultdict(bool)
    res = 0
    def next(depth) :
        nonlocal res
        if depth == N :
            res += 1
            return
        
        for col in range(N) :
            leftKey = depth + col
            rightKey = depth - col
            if colVisited[col] or leftVisited[leftKey] or rightVisited[rightKey]:
                continue
            colVisited[col] = True
            leftVisited[leftKey] = True
            rightVisited[rightKey] = True
            next(depth + 1)
            colVisited[col] = False
            leftVisited[leftKey] = False
            rightVisited[rightKey] = False
    next(0)
    print(res)
sol()