import sys

input = sys.stdin.readline
n = int(input())

targets = []
times = []

res = [sys.maxsize] * n
for ind in range(n):
    curInput = list(map(int, input().strip().split()))
    times.append(curInput[0])
    nexts = curInput[1:]
    nexts.pop()
    nexts = list(map(lambda x: x - 1, nexts))
    targets.append(nexts)
    if len(nexts) == 0 :
        res[ind] = times[ind]

def sol(cur: int) :
    global res, targets, times
    if res[cur] != sys.maxsize :
        return res[cur]
    
    for prev in targets[cur]:
        if res[prev] == sys.maxsize :
            sol(prev)
    res[cur] = max(list(map(lambda x: res[x], targets[cur]))) + times[cur]
    return res[cur]

for ind in range(n):
    sol(ind)

print("\n".join(list(map(str, res))))