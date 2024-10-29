import sys
input = sys.stdin.readline

N, K = list(map(int, input().split()))
arr = list(map(int, input().split()))

left = 0
right = 0
cur = [0] * 200_001
cur[arr[0]] += 1
maxVal = 1
while right < N:
    while right + 1 < N :
        curVal = arr[right + 1]
        if cur[curVal] + 1 > K :
            break
        cur[arr[right + 1]] += 1
        right += 1
    maxVal = max(maxVal, right - left + 1)
    if left == right :
        left, right = left + 1, right + 1
    else :
        cur[arr[left]] -= 1
        left += 1
print(maxVal)