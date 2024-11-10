import sys
input = sys.stdin.readline

def sol2():
    N, X = list(map(int, input().split()))
    availableCount = (X - 1000 * N) // 4000
    board = []
    for _ in range(N):
        a, b = list(map(int, input().split()))
        board.append((a, b))

    tInds = list(map(lambda x: 1, range(N)))
    t = []
    if availableCount != 0 :
        for ind, val in enumerate(board) :
            f, s = val[0], val[1]
            if s < f:
                t.append((f - s, ind))
        for _, ind in sorted(t, reverse=True) :
            tInds[ind] = 0
            availableCount -= 1
            if availableCount == 0 :
                break

    res = 0
    for ind, val in enumerate(tInds) :
        res += board[ind][val]
    print(res)

def sol() :
    N, X = list(map(int, input().split()))
    availableCount = (X - 1000 * N) // 4000
    board = []
    for _ in range(N):
        a, b = list(map(int, input().split()))
        board.append((a, b, a - b))
    res = 0
    board = sorted(board, key= lambda x: x[2], reverse= True)
    res += sum(list(map(lambda x: x[0] if x[0] > x[1] else x[1], board[:availableCount])))
    res += sum(list(map(lambda x: x[1], board[availableCount:])))
    print(res)

sol()
# 3 11000
# 31 11
# 22 12
# 53 23