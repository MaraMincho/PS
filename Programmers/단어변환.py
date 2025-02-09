import collections
def solution(begin, target, words):
    answer = 0
    q = collections.deque()
    q.append((begin, []))
    while q and q[0][0] != target:
        curString, visited = q.popleft()
        for ind in range(len(words)) :
            if ind in visited:
                continue
            flagCount = 0
            next = words[ind]
            for v, w in zip(next, curString):
                if v == w:
                    continue
                flagCount += 1
                if flagCount >= 2 :
                    break
            
            if flagCount == 1 :
                q.append((next, visited + [ind]))
    if not q:
        return 0
    return len(q[0][1])