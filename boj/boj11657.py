import sys
input = sys.stdin.readline

(N, M) = list(map(int, input().split()))


board = list(map(lambda _ : sys.maxsize, range(N + 1)))
prev = list(map(lambda _ : None, range(N + 1)))
edges = []
for _ in range(M) :
    v0, v1, w = list(map(int, input().split()))
    edges.append((v0, v1, w))
    

def bf(start) :
    board[start] = 0
    
    for ind in range(N) :
        for edge in edges :
            prev, next, w = edge
            
            if not board[prev] == sys.maxsize and board[next] > board[prev] + w :
                board[next] = board[prev] + w
                if ind == N - 1 :
                    return []
    return board

res = bf(1)
if res :
    res = list(map(lambda x: x if not x == sys.maxsize else -1, res))
    list(map(lambda x: print(x), res[2:]))
else :
    print(-1)
