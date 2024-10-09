
n = 1000 - int(input())
res = 0
for cur in [500, 100, 50, 10, 5, 1] :
    res += n // cur
    n %= cur
print(res)