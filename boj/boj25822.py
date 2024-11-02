import sys
input = sys.stdin.readline

C = float(input())
K = min(int(C // 0.99), 2)
KDays = []
N = int(input())
days = list(map(int, input().split()))
if days[0] == 0 and K > 0 :
    KDays.append(0)

left, right = 0 , 0
maxLength, maxProblemCount = 0, max(days)
while right < N :
    while right + 1 < N :
        if days[right + 1] != 0 :
            right += 1
        elif len(KDays) < K :
            KDays.append(right + 1)
            right += 1
        else :
            break
    # K = 0이면서,  left, right 가 같으며 days[left] == 0일 때
    if days[left] == 0 and left not in KDays :
        left += 1
        right = left
        continue
    
    currentLength = right - left + 1
    if currentLength > maxLength:
        maxLength = currentLength
    
    if left in KDays :
        KDays.remove(left)
    
    left += 1
    if left < N and days[left] == 0 and left not in KDays and len(KDays) < K:
        KDays.append(left)
    
    if right < left :
        right = left

print(maxLength)
print(max(days))

# 3
# 7
# 0 20 0 0 0 7 0

# 3
# 7
# 0 9 0 0 0 20 0
# answer
# 3
# 20

# 1
# 7
# 0 20 0 0 1 2 0
# answer 
# 3
# 2