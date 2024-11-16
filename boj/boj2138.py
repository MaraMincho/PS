import sys
input = sys.stdin.readline

spinDir = {1: 0, 0: 1}

def spin(board, ind) :
    N = len(board)
    if 0 <= ind - 1 :
        board[ind - 1] = spinDir[board[ind - 1]]
    board[ind] = spinDir[board[ind]]
    if ind + 1 < N :
        board[ind + 1] = spinDir[board[ind + 1]]

def sol() :
    N = int(input())
    original = list(map(int, input().strip()))
    target = list(map(int, input().strip()))
    
    temp, tempCount = original[:] , 0
    for ind in range(1, N) :
        if temp[ind - 1] != target[ind - 1] :
            spin(temp, ind)
            tempCount += 1
    res = tempCount if temp == target else sys.maxsize
    
    temp, tempCount = original[:], 1
    spin(temp, 0)
    for ind in range(1, N) :
        if temp[ind - 1] != target[ind - 1] :
            spin(temp, ind)
            tempCount += 1
    res = min(res, tempCount if temp == target else sys.maxsize)
    
    print(res if res != sys.maxsize else -1)
sol()