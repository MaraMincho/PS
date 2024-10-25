import sys
import collections
input = sys.stdin.readline
## https://maramincho.tistory.com/157

def sol() :
    curInput = input().strip()
    q = collections.deque()
    q.append(curInput)
    
    flag = False
    visited = collections.defaultdict(lambda: False)
    while not flag and q :
        curInput = q.popleft()
        temp = list(map(str, curInput[:]))
        tempInd = 1
        curList = []
        while tempInd < len(temp) :
            prev = temp[tempInd - 1]
            cur = temp[tempInd]
            if prev == cur :
                prevStartInd = tempInd - 1
                while tempInd < len(temp) and prev == temp[tempInd] :
                    tempInd += 1
                curList.append((prevStartInd, tempInd - 1))
            else :
                tempInd += 1
        for startInd, endInd in curList :
            nextCur = list(map(str, curInput[:]))
            for ind in range(startInd, endInd + 1) :
                nextCur[ind] = ""
            nextCur = "".join(nextCur)
            if nextCur == "" :
                flag = True
                break
            if not visited[nextCur] :
                visited[nextCur] = True
                q.append(nextCur)
    return 1 if flag else 0

def sol2() :
    curInput = input().strip()
    def spiltInput(curInput: str)  :
        curStr = curInput[0]
        res = []
        for ele in curInput[1:] :
            if curStr[0] == ele :
                curStr += ele
            else :
                res.append(curStr)
                curStr = ele
        res.append(curStr)
        return res
    visited = collections.defaultdict(lambda: False)

    def dfs(strList: list) :
        strList = spiltInput("".join(strList))
        if len(strList) == 1 :
            return 0 if len(strList[0]) == 1 else 1
        for ind in range(len(strList)) :
            if len(strList[ind]) >= 2 :
                newList = strList[:]
                newList.pop(ind)
                if visited[tuple(newList)] == False :
                    visited[tuple(newList)] = True
                    curRes = dfs(newList)
                    if curRes == 1 :
                        return 1
        return 0
    return dfs(spiltInput(curInput))

res = []
for _ in range(int(input())) :
    res.append(sol2())

[print(x) for x in res]