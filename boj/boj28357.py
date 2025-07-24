import sys

input = sys.stdin.readline

N, K = list(map(int, input().split()))
board = list(map(int, input().split()))
board.sort()

lo = 0
hi = board[-1]

def f(v):
    lo =  0
    hi = len(board)
    
    while lo + 1 < hi :
        mid = (lo + hi) // 2
        if v > board[mid] :
            lo = mid
        else :
            hi = mid
    return hi

def s(v):
    ind = f(v)
    x = board[ind:]
    return sum(x) - (len(x) * v)

while lo + 1 < hi :
    mid = (lo + hi) // 2
    if s(mid) > K:
        lo = mid
    else :
        hi = mid
print(hi)

