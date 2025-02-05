import math
def solution(arrayA, arrayB):
    answer = 0
    
    def k(val):
        answer = val[0]
        for next in val[1:] :
            answer = math.gcd(next)
        return answer
        
        
    return answer

# print(solution([8, 2, 4], [4, 5, 7]))