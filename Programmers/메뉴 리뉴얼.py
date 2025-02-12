import itertools
import collections

def solution(orders, course):
    orders = list(map(lambda x: sorted(x), orders))
    d = collections.defaultdict(int)
    
    # 모든 조합의 등장 횟수 카운트
    for order in orders:
        for combinationCount in course:
            for elements in itertools.combinations(order, combinationCount):
                d["".join(elements)] += 1
    
    visited = {ind: 0 for ind in course}
    res = []
    
    # 최다 주문 조합 찾기
    for key, value in sorted(d.items(), key=lambda x: [-x[1], -len(x[0]), x[0]]):
        visitedKey = len(key)
        if value > 1 and visited[visitedKey] <= value:
            visited[visitedKey] = value
            res.append(key)
    
    return sorted(res)
