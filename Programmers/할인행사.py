import collections
def solution(want, number, discount):
    # (key: 아이템, value: visitedIndex)
    wantDict = {}
    for (item, number) in zip(want, number) :
        wantDict[item] = number
    
    def check(d1, d2) :
        nonlocal want
        for item in want :
            if d1.get(item) != d2.get(item, None) :
                return False
        return True

    answer = 0
    td = collections.defaultdict(int)
    for index, curItem in enumerate(discount) :
        td[curItem] += 1
        
        if index >= 10:
            prevItem = discount[index - 10]
            td[prevItem] -= 1

        if index >= 9 and check(wantDict, td) :
            answer += 1
        
    return answer