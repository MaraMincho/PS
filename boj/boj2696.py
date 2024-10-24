import sys
import heapq
input = sys.stdin.readline

def sol() :
    n = int(input())
    recursionCount =  (n // 10) + (1 if n % 10 != 0 else 0)
    arr = []
    for _ in range(recursionCount):
        cur = list(map(int, input().split()))
        arr += cur
    ## max Heap, min Heap, list<int>
    left, right, res = [-arr[0]], [], [arr[0]]
    for ind in range(1, n):
        cur = arr[ind]
        heapq.heappush(right, cur)
        if ind % 2 == 0 :
            popVal = heapq.heappop(right)
            heapq.heappush(left, -popVal)
            while left and right and right[0] < -left[0] :
                leftPopVal = -heapq.heappop(left)
                rightPopVal = heapq.heappop(right)
                heapq.heappush(left, -rightPopVal)
                heapq.heappush(right, leftPopVal)
            
            res.append(-left[0])
    return list(map(str, res))

for _ in range(int(input())):
    curRes = sol()
    print(len(curRes))
    ind = 0
    while ind < len(curRes) :
        endInd = ind + 10 if ind + 10 < len(curRes) else len(curRes)
        print(*curRes[ind: endInd])
        ind += 10