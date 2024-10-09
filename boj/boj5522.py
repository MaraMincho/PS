import sys

input = sys.stdin.readline
sa = []
for _ in range(5):
    sa.append(int(input()))
print(sum(sa))