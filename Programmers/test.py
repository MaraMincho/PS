def solution(sequence):
    lo, hi = 0, 0
    
    answer = max(list(map(lambda x: abs(x), sequence)))
    while lo < len(sequence):
        cur = sequence[lo]
        prev = cur
        
        while hi + 1 < len(sequence) and prev * sequence[hi + 1] <= 0:
            hi += 1
            prev = sequence[hi]
        
        t = sequence[lo: hi + 1]
        answer = max(answer, sum(list(map(lambda x: abs(x), t))))
        lo = hi + 1
        hi = lo
        
    return answer

print(solution([2, 3, -6, 1, 3, -1, 2, 4]	))