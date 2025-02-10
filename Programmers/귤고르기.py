def solution(k, tangerine):
    d = {}
    for t in tangerine :
        d[t] = d.get(t, 0) + 1
    
    sd = sorted(d.items(), key= lambda x: [-x[1]])
    tk = 0
    answer = 0
    for (key, count) in sd :
        answer += 1
        tk += count
        if k <= tk :
            break
    
    return answer