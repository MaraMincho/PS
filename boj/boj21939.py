import sys
import heapq
input = sys.stdin.readline

## 추가하는건 그냥 추가 
## maxHeap, minheap따로 관리
## visiteid존재. 만약 recommended요청이 들어왔을 경우 key값을 이용해 방문했는지 여부를 검사

def makeKey(level: int, problem: int) -> str:
    return str(problem) + "-" + str(level)

def sol() :
    visited = {}
    maxHeap, minHeap = [], []
    problemAndLevel = {}
    
    for _ in range(int(input())) :
        problemNumber, level  = list(map(int, input().split()))
        prevLevel = problemAndLevel.get(problemNumber)
        if prevLevel != None :
            visited[makeKey(level=prevLevel, problem=problemNumber)] = True
        key = makeKey(level=level, problem=problemNumber)
        visited[key] = False
        problemAndLevel[problemNumber] = level
        heapq.heappush(minHeap, (level, problemNumber))
        heapq.heappush(maxHeap, (-level, -problemNumber))

    for _ in range(int(input())) :
        command = input().split()
        if command[0] == "add" :
            problemNumber, level = int(command[1]), int(command[2])
            prevLevel = problemAndLevel.get(problemNumber)
            if prevLevel != None  :
                visited[makeKey(level=prevLevel, problem=problemNumber)] = True
            key = makeKey(level=level, problem=problemNumber)
            problemAndLevel[problemNumber] = level
            visited[key] = False
            heapq.heappush(minHeap, (level, problemNumber))
            heapq.heappush(maxHeap, (-level, -problemNumber))
        elif command[0] == "recommend" :
            ## 맥스 힙
            if command[1] == "1":
                level, problemNumber = -maxHeap[0][0], -maxHeap[0][1]
                key = makeKey(level=level, problem=problemNumber)
                while visited[key] :
                    heapq.heappop(maxHeap)
                    element = maxHeap[0]
                    level, problemNumber = -element[0], -element[1]
                    key = makeKey(level=level, problem=problemNumber)
                print(problemNumber)
            ## 민ㅇ힙
            else :
                level, problemNumber = minHeap[0]
                key = makeKey(level=level, problem=problemNumber)
                while visited[key] :
                    heapq.heappop(minHeap)
                    level, problemNumber = minHeap[0]
                    key = makeKey(level=level, problem=problemNumber)
                print(problemNumber)
        else :
            problemNumber = int(command[1])
            level = problemAndLevel[problemNumber]
            key = makeKey(level=level, problem=problemNumber)
            visited[key] = True
sol()