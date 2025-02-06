import collections
def solution(n, results):
    board = list(map(lambda x: [0] * (n), range(n)))
    for (v0, v1) in results :
        board[v1 - 1][v0 - 1] = 1
        board[v0 - 1][v1 - 1] = -1
    
    for mid in range(n) :
        for s in range(n) :
            for e in range(n):
                if board[s][mid] == board[mid][e] :
                    board[s][e] = board[s][mid]
                    board[e][s] = -board[s][mid]
    answer = 0
    for col in range(board) :
        if len(list(filter(lambda x: x == 0, col))) == 1 :
            answer += 1
    return answer

print(solution(5,	[[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))