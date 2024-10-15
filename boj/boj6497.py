import sys
from functools import cmp_to_key


def sol(n, m) :
    input = sys.stdin.readline
    ## [(a0, a1, w)]
    routes = []
    for _ in range(m):
        routes.append(list(map(int, input().split())))

    routes.sort(key= lambda x: [x[2]])

    unions = [i for i in range(n)]

    def findParent(val: int) -> int :
        nonlocal unions
        if unions[val] != val :
            return findParent(unions[val])
        return val
    res = 0
    for (f, t, w) in routes :
        fp, tp = findParent(f), findParent(t)
        if fp == tp :
            continue
        res += w
        if fp < tp :
            unions[t] = fp
            unions[tp] = fp
        else :
            unions[f] = tp
            unions[fp] = tp
    res = sum([x[2] for x in routes]) - res
    print(res)


while True:
    (n, m) = list(map(int, input().split()))
    if n == m == 0 :
        break
    sol(n, m)