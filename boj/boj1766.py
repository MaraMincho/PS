import sys
import collections
import heapq
input = sys.stdin.readline
(N, M) = list(map(int, input().strip().split()))

## 내 입장에서 꼭 풀어야하는 문제들
recommend = collections.defaultdict(list)
## 내가 해결되었을 때 영향을 미치는 문제들
effect = collections.defaultdict(list)

for _ in range(M) :
    (child, parent) = list(map(int, input().strip().split()))
    recommend[parent].append(child)
    effect[child].append(parent)

solved = [False] * (N + 1)
res = []

curHeap = []

def pushCurHeap(cur: int):
    global curHeap, effect, recommend, solved
    for ele in effect[cur] :
        solvedFlag = True
        for c in recommend[ele]:
            if solved[c] == False :
                solvedFlag = False
                break
        if solvedFlag :
            heapq.heappush(curHeap, ele)


def sol(cur: int) :
    global curHeap, res, solved
    solved[cur] = True
    res.append(cur)
    pushCurHeap(cur)
    while curHeap and -curHeap[-1] < cur:
        next = heapq.heappop(curHeap)
        solved[next] = True
        res.append(next)
        pushCurHeap(next)

for ind in range(1, N + 1):
    if not recommend[ind] :  
        sol(ind)

while curHeap :
    next = heapq.heappop(curHeap)
    sol(next)
    
print(" ".join(map(str, res)))