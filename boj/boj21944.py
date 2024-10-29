import sys
import collections
from heapq import heappush, heappop
input = sys.stdin.readline


isSovled = {}
algorithmAndProblemsMin = collections.defaultdict(lambda: [])
algorithmAndProblemsMax = collections.defaultdict(lambda: [])
def makeKey(L, P, G) :
    return "-".join(list(map(str, [P, L, G])))
for _ in range(int(input())) :
    ## 문제번호, 난이도, 알고리즘 분류
    P, L, G = list(map(int, input().split()))
    isSovled[P] = False
    heappush(algorithmAndProblemsMax[G], [L, P])