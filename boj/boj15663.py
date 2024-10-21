import sys
import itertools
input = sys.stdin.readline

(n, m) = list(map(int, input().split()))
curArr = list(map(int, input().split()))

curArr.sort
res = set()

for val in itertools.permutations(curArr, m) :
    if val in res :
        continue
    res.add(val)
    print(*val)