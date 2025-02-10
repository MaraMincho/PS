def solution(citations):
    paper = citations

    start = 0
    end = max(paper)
    
    while start + 1 < end :
        mid = (start + end) // 2
        t = len(list(filter(lambda x: mid <= x, paper)))
        print(mid, t, start, end)
        v = mid <= t
        if v:
            start = mid
        else :
            end = mid
            
    return start
print(solution([3, 4, 4, 4, 0, 6, 1, 5]))