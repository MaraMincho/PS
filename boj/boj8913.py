import sys
import collections
input = sys.stdin.readline

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


res = []
for _ in range(int(input())) :
    res.append(sol())

[print(x) for x in res]