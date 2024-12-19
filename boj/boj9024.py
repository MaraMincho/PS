import sys
input = sys.stdin.readline

def sol():
    n, k = list(map(int, input().split()))
    board = list(map(int, input().split()))
    board.sort()
    res = sys.maxsize
    resCount = 0
    print(board)
    for ind in range(n - 1) :
        left, right = ind + 1, n - 1
        while left + 1 < right :
            mid = (left + right) // 2
            cur = board[mid] + board[ind]
            if cur < k :
                left = mid
            else :
                right = mid
            if abs(k - cur) < res :
                resCount = 1
                res = abs(k - cur)
            elif abs(k - cur) == res :
                resCount += 1
        print(res, resCount)
    return resCount

res = []     
for _ in range(int(input())):
    res.append(sol())

list(print(x) for x in res)