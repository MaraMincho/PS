import sys
input = sys.stdin.readline


def lcm(v, t) :
    originalV, originalT = v, t
    while v != t :
        if v < t :
            v += originalV
        else :
            t += originalT
    return v

def sol() :
    s, t = list(map(str, input().split()))
    sc, tc = len(s), len(t)
    curLcm = lcm(sc, tc)
    ts = s * (curLcm // sc)
    tt = t * (curLcm // tc)
    return ts == tt

for ind in range(int(input())) :
    answer = "yes" if sol() else "no"
    print(f"#{ind + 1} {answer}")