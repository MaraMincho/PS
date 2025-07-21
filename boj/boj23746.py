import sys

input = sys.stdin.readline
n = int(input())
d = {}
for _ in range(n):
    x, y = input().strip().split()
    d[y] = x
s = input().strip()

ans = ""
for c in s :
    ans += d[c]
s, e = list(map(int, input().split()))
print(ans[s - 1 : e])