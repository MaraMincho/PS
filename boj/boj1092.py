import sys
input = sys.stdin.readline

kCount = int(input())
k = list(map(int, input().split()))
k.sort(reverse= True)

boxesCount = int(input())
boxes = list(map(int, input().split()))
boxes.sort(reverse= True)

tasks = [[] for _ in range(kCount) ] 

res = 0
if boxes[0] > k[0] :
    print(-1)
    exit(0)
while boxes :
    for ind in range(kCount) :
        curK = k[ind]
        if boxes and curK < boxes[-1] :
            break
        for box in boxes :
            if box <= curK :
                boxes.remove(box)
                break
    res += 1
print(res)