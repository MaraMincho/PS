import sys

print(sum(list(map(lambda x: int(x) * int(x), input().split()))) % 10)
