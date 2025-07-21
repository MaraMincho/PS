import sys
import math
import fractions
input = sys.stdin.readline

x = list(map(int, input().split()))
v0, v1 = list(map(lambda x: math.isqrt(int(x)), x))

v0 = int(v0) + 1
v1 = int(v1)
t = v1 - v0 + 1
d = x[1] - x[0]
if t == d :
    print(t, "/", d, sep="")
else:
    print(fractions.Fraction(t, d))