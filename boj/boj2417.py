import sys

left = 0
right = int(sys.maxsize ** 1/2 + 1)
target = int(input())

if target == 0 :
    print(0)
    exit(0)
while left + 1 < right :
    mid = (left + right) // 2
    if mid * mid < target :
        left = mid
    else :
        right = mid
print(right)