import sys

input = sys.stdin.readline

(N, K) = list(map(int, input().split()))
papers = list(map(int, input().split()))

left = 0
right = sum(papers) + 1

def check(targetSum: int) -> bool:
    global papers, K
    
    prev = 0
    resFlag = 0
    for cur in papers:
        prev += cur
        if prev >= targetSum :
            prev = 0
            resFlag += 1
            if resFlag >= K :
                return True
    
    return False
    
while left + 1 < right :
    mid = (left + right) // 2
    if check(mid) :
        left = mid
    else :
        right = mid
print(left)