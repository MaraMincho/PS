import sys
input = sys.stdin.readline

curD = {0 : 0, 1: 1, -1: 3}

prev = -1
while -prev <= 1000000000 :
    lv = prev * 2
    rv = lv * -1
    curD[rv] = curD[prev] + (rv - prev)
    curD[lv] = curD[rv] + (rv - lv)
    prev = lv

def sol() :
    cur = int(input())
    if cur == 0 :
        return 0
    elif 1 == abs(cur) :
        return curD[cur]
    t = 1
    while t * 2 < abs(cur) :
        t *= 2
    
    if cur > 0 :
        t = -t
        return curD[t] + abs(cur - t)
    else :
        t *= 2
        return curD[t] + abs(cur - t)

cur = list(map(lambda _: sol() ,range(int(input()))))
[print(x) for x in cur]