

# 비밀번호의 길이 N, 문자의 종류 개수 M, 정수 A
# 해시값 정수 H

import sys
import copy 
import functools
(N, M, A) = list(map(int, sys.stdin.readline().split()))
H = int(sys.stdin.readline())


resModVal = 1000000000 + 7
res = 1
for _ in range(N - 1):
    res = (res * M) % resModVal
print(res)
# prev = list(map(lambda x: 1, range(M)))

# cur = copy.deepcopy(prev)
# prevElementDict = {}
# for ind in range(M) :
#     if ind > H :
#         tVal = H + M - ind
#         prevElementDict[ind] = tVal
#     else:
#         prevElementDict[ind] = H - ind
# resModVal = 1000000000 + 7
# res = 1
# for _ in range(1, N) :
#     for ind in range(1, M) :
#         curVal = pow(ind, A) % M
#         targetInd = prevElementDict[curVal]
#         willAddValue = prev[targetInd]
#         res = (res + willAddValue) % resModVal
#         cur[targetInd] += 1
#     prev = copy.deepcopy(cur)
# print(res)
