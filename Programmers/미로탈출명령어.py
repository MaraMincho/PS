# d(아래), l(왼쪽), r(오른쪽), u(위쪽)
def solution(n, m, x, y, r, c, k):
    dirs = [("d", (1, 0)), ('l', (0, -1)), ('r', (0, 1)), ('u', (-1, 0))]
    s = (x, y)
    e = (r, c)
    
    # 구해야 할 것들
    # 이동하는 최적의 루트
    # 현 자리에서 왔다리 갔다리 할 수 있는지(중요)
    # Impossible한지
    
    def getD(s, e):
        return abs(s[0] - e[0]) + abs(s[1] - e[1])
    def isOk(cur):
        nonlocal n, m
        return 1 <= cur[0] <= n and 1 <= cur[1] <= m
    e0 = getD(s,e )
    
    # Impossible 로직
    if k < e0 or (k - e0) % 2 == 1:
        return "impossible"
    
    # e0 list 구하기 
    e1Count = (k - e0) // 2
    
    cur = s
    answer = ""
    def re(cur):
        nonlocal answer, e1Count
        for (curString, dir) in dirs :
            flag = False
            while True :
                prevAbs = getD(cur, e)
                next = (cur[0] + dir[0], cur[1] + dir[1])
                nextAbs = getD(next, e)
                if isOk(next) and nextAbs <= prevAbs :
                    flag = True
                    answer += curString
                    cur = next
                elif isOk(next) and (e1Count) > 0 :
                    flag = True
                    e1Count -= 1
                    answer += curString
                    cur = next
                else:
                    break
                # 남은 거리가 존재하면서, "r", 이나 "u"는 다시 solution loop을 돌아야만 합니다. 
                rest = (k - len(answer)) - getD(cur, e)
                if not rest == 0 and curString in ["r", "u"]:
                    break
            if flag :
                return cur
        return cur
    while not len(answer) == k:
        cur = re(cur)
    
    return answer