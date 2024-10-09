import heapq
import sys

## max Heap
left = []
lc = 0
## min Heap
right = []
rc = 0
res = []
for ind in range(int(sys.stdin.readline())) :
    cur = int(sys.stdin.readline())
    if left == [] :
        left.append(-cur)
        res.append(str(cur))
        lc += 1
    elif right == [] :
        if -left[0] > cur :
            right.append(-left[0])
            left[0] = -cur
            
        else :
            right.append(cur)
        res.append(-left[0])
        rc += 1
    else :
        if -left[0] < cur :
            heapq.heappush(right, cur)
            rc += 1
        else :
            heapq.heappush(left, -cur)
            lc += 1
        
        while lc > rc :
            popValue = -heapq.heappop(left)
            heapq.heappush(right, popValue)
            lc -= 1
            rc += 1
        
        while lc < rc :
            popValue = heapq.heappop(right)
            heapq.heappush(left, -popValue)
            lc += 1
            rc -= 1
          
        
        if ind % 2 == 0 :
            res.append(min(-left[0], right[0]))
        else :
            res.append(-left[0]) 
res = list(map(str, res))
print("\n".join(res))