import sys
input = sys.stdin.readline

# 고양이 N 마리, 과자 M 개
# 과자는 i 번째 과자는 Vj 조각으로 쪼개짐
# i번째 고양이가 먹은 j번 과자의 조각 수는 Aji

# 출력은 기약 분수로 형태로 출력한다. 

def gcd(a, b) :
    if a == 0 :
        return b
    return gcd(b % a, a)

def lcm(a, b) :
    return (a * b) // gcd(a, b)

def xx(a, b) :
    curGCD = gcd(a, b) if a < b else gcd(b, a)
    return (a // curGCD, b // curGCD)

def sol() :
    N, M = list(map(int, input().split()))
    cats = [(0, 1)] * N
    for _ in range(M) :
        cur = list(map(int, input().split()))
        for catInd in range(N):
            if cur[catInd + 1] == 0 :
                continue
            prev = cats[catInd]
            curLcmTarget = (prev[1], cur[0]) if prev[1] < cur[0] else (cur[0], prev[1])
            curLcm = lcm(curLcmTarget[0], curLcmTarget[1])
            u = (curLcm // cur[0]) * cur[catInd + 1]
            p = (curLcm // prev[1]) * prev[0] 
            cats[catInd] = xx(u + p, curLcm)
    minVal = min(cats, key=lambda x: x[0] / x[1])
    maxVal = max(cats, key=lambda x: x[0] / x[1])
    
    curLcmTarget = (minVal[1], maxVal[1]) if minVal[1] < maxVal[1] else (maxVal[1], minVal[1])
    curLcm = lcm(curLcmTarget[0], curLcmTarget[1])
    u = (curLcm // minVal[1]) * minVal[0]
    p = (curLcm // maxVal[1]) * maxVal[0]
    res = xx(p - u , curLcm)
    if res[1] == 1 :
        print(res[0])
    else :
        print(f'{res[0]}/{res[1]}')
    


import fractions

cur = fractions.Fraction(3, 5)

for _ in range(int(input())):
    N, M = list(map(int, input().split()))
    
    cats = list(map(lambda _: fractions.Fraction(0, 1), range(N)))
    for _ in range(M) :
        cur = list(map(int, input().split()))
        for catInd in range(N):
            cats[catInd] += fractions.Fraction(cur[catInd + 1], cur[0])
    maxCat = max(cats)
    minCat = min(cats)
    print(maxCat - minCat)