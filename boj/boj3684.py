
import sys
input = sys.stdin.readline

T = int(input())
s = [int(input()) for _ in range(T)]

if T == 1:
    print(1)
    sys.exit(0)    

c = 10001
def cc(v, a, b):
    return (a * v + b) % c

for n1 in range(0, c):
    for n2 in range(0, c):
        res = [cc(s[0], n1, n2)]
        flag = True
        for e in s[1:]:
            if cc(res[-1], n1, n2) != e:
                flag = False
                break
            res.append(cc(e, n1, n2))
        if flag:
            [print(x) for x in res]
            exit(0)