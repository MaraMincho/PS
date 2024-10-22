import sys
input = sys.stdin.readline
N, Q = list(map(int, input().split()))
arr = list(map(int, input().split()))
arr.sort()
sumArr = [arr[0]]
for ind in range(1, N):
    sumArr.append(arr[ind] + sumArr[-1])
res = []
for _ in range(Q):
    startV, toV = list(map(lambda x: int(x) - 1, input().split()))
    tempSum = sumArr[toV]
    if 0 < startV :
        tempSum -= sumArr[startV - 1]
    res.append(str(tempSum))
[print(x) for x in res]