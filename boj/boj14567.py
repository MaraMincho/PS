import sys
import collections

input = sys.stdin.readline

(n, m) = list(map(int, input().split()))

s = collections.defaultdict(list)
c = [0] * (n + 1)
for _ in range(m):
    (prev, next) = list(map(int, input().split()))
    s[prev].append(next)
    c[next] += 1

res = [1] * (n + 1)
q = collections.deque()
def ts(cur: int) :
    global res, s, c
    for next in s[cur] :
        c[next] -= 1
        if c[next] == 0 :
            res[next] = res[cur] + 1
            q.append(next)

for cur in range(1, n + 1)   :
    if c[cur] == 0 :
        q.append(cur)
while q:
    cur = q.popleft()
    ts(cur)

print(" ".join(list(map(str, res[1:]))))