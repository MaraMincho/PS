import sys

input = sys.stdin.readline

n = int(input())
x = sorted(list(map(int, input().split())), reverse=True)
ans = 0
while x :
    cur = x.pop()
    ans += 1
    for _ in range(1, cur):
        if not x:
            break
        x.pop()

print(ans)
