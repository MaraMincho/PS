import sys
import itertools
import functools
input = sys.stdin.readline

def sol(x: int) -> list:
    res = []
    for i in itertools.product(["0", "1"], repeat=x) :
        cur = functools.reduce(lambda x, y: x + y, i, "")
        res.append(cur)
    return res

tVal = int(input())
tt = []
prev = 1
while len(tt) < tVal :
    tt += sol(prev)
    prev += 1
di = {"0": "4", "1": "7"}
convertVal = "".join(list(map(lambda x: di[x], tt[tVal - 1])))
print(convertVal)

## 0 -> 1
## 00 -> 01 -> 10 -> 11