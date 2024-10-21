import itertools
import sys
sys.setrecursionlimit(10000)

def permutations( arr: list, m: int) :
    visited = [False] * len(arr)
    tempRes = []
    res = []
    
    def fc() :
        nonlocal tempRes, visited, res, arr, m
        if len(tempRes) == m :
            res.append(tempRes[:])
        for ind in range(len(arr)):
            if visited[ind] == True :
                continue
            visited[ind] = True
            tempRes.append(arr[ind])
            fc()
            visited[ind] = False
            tempRes.pop()
    fc()
    return res
print(permutations([1, 2, 3, 4], 2))

def combinations( arr: list, m: int) :
    tempRes = []
    res = []
    curInd = 0
    def fc() :
        nonlocal arr, tempRes, res, m, curInd
        if len(tempRes) == m:
            res.append(tempRes[:])
            return 
        elif curInd >= len(arr) :
            return
        for ind in range(curInd, len(arr)):
            curVal = arr[ind]
            tempRes.append(curVal)
            curInd = ind + 1
            fc()
            curInd = ind
            tempRes.pop()
    fc()
    return res
print(combinations([1, 2, 3, 4, 5, 6], 4))