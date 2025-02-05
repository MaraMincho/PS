import sys
def solution(n, s, a, b, fares):
    answer = sys.maxsize
    
    # A, B 간선을 거치는 최저 비용
    # A, B 합승하다 중간에 내릴 수 있음
    # 2 < n < 100 이니까 부르스트포스
    # table만들고 모든 점을 돌면서 거리 구하기
    maxsize = sys.maxsize // 2
    board = list(map(lambda x: [maxsize] * (n + 1), range(n + 1)))
    
    for ind in range(1, n + 1) :
        board[ind][ind] = 0
    
    for (v0, v1, w) in fares:
        board[v0][v1] = w
        board[v1][v0] = w
    
    for mid in range(1, n + 1) :
        for v0 in range(1, n + 1):
            for v1 in range(1, n + 1) :
                if board[v0][v1] > board[v0][mid] + board[mid][v1] :
                    board[v0][v1] = board[v0][mid] + board[mid][v1]
    
    for mid in range(1, n + 1) :
        if answer > board[s][mid] + board[mid][a] + board[mid][b] :
            answer = board[s][mid] + board[mid][a] + board[mid][b] 
    
    return answer