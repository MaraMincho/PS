import sys
input = sys.stdin.readline

C = float(input())
K = int(C / 0.99)
K = K if K <= 2 else 2
KDays = []
N = int(input())
days = list(map(int, input().split()))

left = 0
right = 0
maxLength = 1
maxProblemCount = 0
if days[0] == 0 :
    if len(KDays) < K :
        KDays.append(0)

while right < N :
    while right + 1 < N:
        if days[right + 1] > 0 :
            right += 1
        elif len(KDays) < K :
            right += 1
            KDays.append(right)
        else :
            break
    currentSequenceLength = right - left + 1
    if maxLength <= currentSequenceLength :
        targetList = list(map(lambda x: days[x], range(left, right + 1)))
        if maxLength == currentSequenceLength :
            maxProblemCount = max([maxProblemCount] + targetList)
        else :
            maxProblemCount = max(targetList)
        maxLength = currentSequenceLength

    if left in KDays :
        KDays.remove(left)

    left += 1
    if left < N and days[left] == 0 and len(KDays) < K and left not in KDays:
        KDays.append(left)

    if right < left :
        right = left
print(maxLength)
print(maxProblemCount)

# 3
# 7
# 0 20 0 0 0 7 0

# 3
# 7
# 0 9 0 0 0 20 0

# 1
# 7
# 0 20 0 0 1 2 0