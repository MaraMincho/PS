import sys
import heapq
input = sys.stdin.readline

def sol() :
    minq = []
    maxq = []
    n = int(input())
    visited = {}
    for _ in range(n):
        s, val = input().split()
        val = int(val)
        
        if s == "I" :
            minval = val
            maxval = -val
            heapq.heappush(minq, minval)
            heapq.heappush(maxq, maxval)
            visited[val] = visited[val] + 2 if visited.get(val) else 2
        elif s == "D" and val == -1:
            while minq and True :
                cur = heapq.heappop(minq)
                if visited[cur] == 0:
                    continue
                visited[cur] -= 1
                if visited[cur] % 2 == 1 :
                    visited[cur] -= 1
                    break
        elif s == "D" and val == 1:
            while maxq and True :
                cur = -heapq.heappop(maxq)
                if visited[cur] == 0:
                    continue
                visited[cur] -= 1
                if visited[cur] % 2 == 1 :
                    visited[cur] -= 1
                    break
    visited = list(filter(lambda x: x[1] != 0, visited.items()))
    if not visited :
        print("EMPTY")
        return
    maxVal = max(visited, key=lambda x: x[0])[0]
    minVal = min(visited, key= lambda x: x[0])[0]
    print(maxVal, minVal)

for _ in range(int(input())):
    sol()
