import sys
import collections
input = sys.stdin.readline

(N, d, k, c) = list(map(int, input().split()))

cho = []
for _ in range(N) :
    cho.append(int(input()))

cur = [0] * (d + 1)
cur[c] += 1
res = 1
for ind in range(N - k + 1, N) :
    cur[cho[ind]] += 1
    if cur[cho[ind]] == 1 :
        res += 1
    
curCount = res
for ind in range(N) :
    cur[cho[ind]] += 1
    if cur[cho[ind]] == 1 :
        curCount += 1

    if res < curCount :
        res = curCount
        if res == k + 1 :
            print(k + 1)
            exit(0)

    cur[cho[ind - k + 1]]  -= 1
    if cur[cho[ind - k + 1]] == 0 :
        curCount -= 1
print(res)