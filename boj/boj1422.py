import sys
from functools import cmp_to_key

input = sys.stdin.readline

(N, K) = map(int, input().split())

nums = []
for _ in range(N):
    nums.append(input().strip())


def sortFunc(x: str, y: str) :
    if x + y < y + x :
        return 1
    else :
        return -1

nums.sort(key=cmp_to_key(sortFunc))
res = ""

flag = False
maxVal = str(max(map(int, nums)))
for num in nums:
    if flag == False and num == maxVal :
        res += num * (K - N)
        flag = True
    res += num
print(res)