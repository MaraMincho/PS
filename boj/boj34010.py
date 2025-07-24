import sys
import collections
input = sys.stdin.readline

N = int(input())

d = {}
v = {}
for i in range(N):
    a0 = list(map(int, input().split()))
    
    for j in range(N - 1):
        d[((i, j), (i, j + 1))] = a0[j]
    if i == N - 1 :
        break
    a1 = list(map(int, input().split()))
    for j in range(N):
        d[((i, j), (i + 1, j))] = a1[j]


q = collections.deque()
q.append((0,0))
