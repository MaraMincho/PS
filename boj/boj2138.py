import sys
input = sys.stdin.readline


def spin(val) :
    return 0 if val == 1 else 1
def sol() :
    N = int(input())
    original = list(map(int, input().strip()))
    target = list(map(int, input().strip()))
    
    temp = original[:]
    tempCount = 0
    for ind in range(1, N) :
        if temp[ind - 1] != target[ind - 1] :
            temp[ind - 1] = spin(temp[ind - 1])
            temp[ind] = spin(temp[ind])
            if ind + 1 < N :
                temp[ind + 1] = spin(temp[ind + 1])
            tempCount += 1
    res = tempCount if temp == target else sys.maxsize
    temp = original[:]
    temp[0] = spin(temp[0])
    temp[1] = spin(temp[1])
    tempCount = 1
    for ind in range(1, N) :
        if temp[ind - 1] != target[ind - 1] :
            temp[ind - 1] = spin(temp[ind - 1])
            temp[ind] = spin(temp[ind])
            if ind + 1 < N :
                temp[ind + 1] = spin(temp[ind + 1])
            tempCount += 1
    res = min(res, tempCount if temp == target else sys.maxsize)
    print(res if res != sys.maxsize else -1)
sol()