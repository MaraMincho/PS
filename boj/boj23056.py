import sys
import collections
import functools
input = sys.stdin.readline

board = collections.defaultdict(lambda : 0)
N, M = list(map(int, input().split()))

res = []
while True :
    (v0, v1) = input().split()
    if v0 == v1 == "0" :
        break
    if board[v0] < M :
        res.append(f'{v0} {v1}')
        board[v0] += 1

def mySort(v0: str, v1: str) :
    l0, r0 = v0.split()
    l1, r1 = v1.split()
    l0, l1 = int(l0), int(l1)
    
    # 청팀을 먼저, 백팀을 나중에 출력한다.
    if l1 % 2 == l0 % 2 :
        if l0 == l1 :
            ## 길이가 같다면 사전 순으로 출력한다.
            if len(r0) == len(r1) :
                return -1 if r0 < r1 else 1
            return -1 if len(r0) < len(r1)  else 1
        return -1 if l0 < l1 else 1
    return -1 if (l0 % 2) > (l1 % 2) else 1
    
res.sort(key=functools.cmp_to_key(mySort))
print("\n".join(res))
