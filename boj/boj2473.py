import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
nums = sorted(nums)

def find(left, right) -> int :
    originalValue = nums[left] + nums[right]
    left, right = left + 1, right - 1
    while left + 1 < right :
        mid = (left + right) // 2
        if originalValue + nums[mid] < 0 :
            left = mid
        else :
            right = mid
    return left if abs(originalValue + nums[left]) < abs(originalValue + nums[right]) else right

flagValue = sys.maxsize
flagNums = []
left, right = 0, n - 1
while flagValue != 0 and left + 1 < right :
    currentSideSum = nums[left] + nums[right]
    findInd = find(left= left, right = right)
    curValue = nums[findInd] + currentSideSum
    if abs(curValue) < flagValue :
        flagValue = abs(curValue)
        flagNums = [left, findInd, right]
    if currentSideSum < 0:
        left += 1
    else :
        right -= 1

print(*list(map(lambda x: str(nums[x]), flagNums)))

