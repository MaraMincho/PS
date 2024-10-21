import itertools

(n, m) = list(map(int, input().split()))
res = itertools.combinations(list(range(1, n + 1)), m)
[print(*x) for x in res]