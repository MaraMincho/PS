import sys
input = sys.stdin.readline

m, n = list(map(int, input().split()))
t = []
for _ in range(n) :
    v, b = list(map(int, input().split()))
    t.append((v, b, v // b))
# 중요도, 필요 시간, 가중치
t.sort(key=lambda x: [x[1]])
# 쓴거, 안쓴거
board = list(map(lambda _: [(0, 0)] * (m + 1), range(n + 1)))
for ind in range(1, n + 1) :
    curV, curB, curW = t[ind - 1]
    for col in range(1, m + 1) :
        
        if curB > col :
            board[ind][col] = (max(board[ind-1][col]), 0)
            continue
        
        # 썼을 경우의 최대
        v0 = max(max(board[ind - 1][col]), board[ind][col - curB][0])
        v1 = max(board[ind][col - curB][0] + curV, board[ind][col - curB][1])
        board[ind][col] = (v0, v1)

print(max(board[-1][-1]))