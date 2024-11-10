import sys
input = sys.stdin.readline

def sol() :
    N = int(input())
    board = list(map(int, input().split()))
    
    board = sorted(board)
    res = 0
    for ind in range(N - 2):
        cur = board[ind]
        start, end = ind + 1, N - 1
        while start < end :
            tempSum = cur + board[start] + board[end]
            if tempSum > 0 :
                end -= 1
            elif tempSum < 0 :
                start += 1
            else :
                if board[start] == board[end] :
                    count = end - start + 1
                    res += (count *  (count - 1)) // 2
                    break
                leftCount = 1
                while board[start] == board[start + 1] :
                    start += 1
                    leftCount += 1
                rightCount = 1
                while board[end] == board[end - 1] :
                    end -= 1
                    rightCount += 1
                res += leftCount * rightCount
                start += 1
                end -= 1
    print(res)
sol()