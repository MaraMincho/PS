import collections
import sys
input = sys.stdin.readline
T = int(input())
n = int(input())
a1 = list(map(int, input().split()))

m = int(input())
a2 = list(map(int, input().split()))

a1s = [a1[0]]
for ind in range(1, n):
    prevSum = a1s[ind -1]
    cur = a1[ind]
    a1s.append(cur + prevSum)

a2s = [a2[0]]
for ind in range(1, m):
    prevSum = a2s[ind - 1]
    cur = a2[ind]
    a2s.append(cur + prevSum)


a1d = collections.defaultdict(int)
a2d = collections.defaultdict(int)

for i in range(n):
    for ind in range(n - i):
        left = ind
        right = ind + i
        a1d[a1s[right] - a1s[left] + a1[left]] += 1

for i in range(m):
    for ind in range(m - i):
        left = ind
        right = ind + i
        a2d[a2s[right] - a2s[left] + a2[left]] += 1

a1ks = list(map(lambda x: x[0], a1d.items()))
res = 0
for a1k in a1ks :
    a2k = T - a1k
    res += a1d[a1k] * a2d[a2k]
print(res)