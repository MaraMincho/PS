import sys
import collections
input = sys.stdin.readline

graph = collections.defaultdict(list)
vertexs = set()
for _ in range(int(input())):
    startV, endV = list(map(str, input().strip().split(sep= " => ")))
    if startV == endV :
        continue
    graph[startV].append(endV)
    vertexs.add(startV)
    vertexs.add(endV)

# str : int
vertexDict = {}
indDict = {}
curCount = 0
board = [[False for _ in range(len(vertexs))] for _ in range(len(vertexs))]
for vertex in sorted(list(vertexs)) :
    vertexDict[vertex] = curCount
    indDict[curCount] = vertex
    board[curCount][curCount] = True
    curCount += 1

for vertex in vertexs :
    for next in graph[vertex]:
        row = vertexDict[vertex]
        col = vertexDict[next]
        board[row][col] = True

for interval in range(len(vertexs)) :
    for sInd in range(len(vertexs)) :
        for eInd in range(len(vertexs)) :
            if board[sInd][eInd] == True :
                continue
            elif board[sInd][interval] == board[interval][eInd] == True:
                board[sInd][eInd] = True
answer = []

for sInd in range(len(vertexs)) :
    for eInd in range(len(vertexs))  :
        if sInd == eInd or board[sInd][eInd] == False :
            continue
        start, end = indDict[sInd], indDict[eInd]
        answer.append(f"{start} => {end}")
print(len(answer))
[print(x) for x in answer]


# 9
# a => b
# b => c
# c => a
# D => a
# A => B
# B => C
# AA => BB
# BB => CC
# CC => AA

# 6
# a => b
# b => c
# c => a
# AA => BB
# BB => CC
# CC => AA