import sys
input = sys.stdin.readline

res = []
for ind in range(int(input())):
    n, m = list(map(int, input().split()))
    val = bin(m)
    legnth = len(val)

    if "1" * n == val[legnth - n:] :
        res.append("ON")
        continue
    res.append("OFF")
for ind, val in enumerate(res) :
    print(f"#{ind + 1} {val}")