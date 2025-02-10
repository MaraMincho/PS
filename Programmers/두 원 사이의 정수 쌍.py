import math

def distance(r, y) :
    if r < y :
        return 0
    value =  int(r ** 2) - int(y ** 2)
    return math.sqrt(value)

def solution(r1, r2):
    answer = 0
    
    for row in range(r2 + 1) :
        ld = distance(r1, row)
        rd = distance(r2, row)
        
        ld = math.ceil(ld)
        rd = int(rd)
        answer += rd - ld + 1
    answer = answer * 4
    answer -= 4 * (r2 - r1 + 1)
    return answer

print(solution(2, 3))