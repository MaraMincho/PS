import functools
import sys
import itertools

(n, m) = list(map(int, sys.stdin.readline().split()))

curList = list(map(lambda x: x + 1, range(n)))

for val in itertools.permutations(curList, m) :

    cur = list(map(lambda x: str(x), val))
    print(" ".join(cur))
    # for cur in val:
    #     print(cur, end=" ")
    # print()