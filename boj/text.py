import sys
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
m0, m1 = list(map(int, sys.stdin.readline().split()))

res = 0
for cur in a :
    temp = (cur - m0) // m1
    if cur - m0 < 0 :
        res += 1
        continue
    sVal = temp if (cur - m0) % m1 == 0 else temp + 1
    res += 1 + sVal
print(res)