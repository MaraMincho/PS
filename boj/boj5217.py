import sys
input = sys.stdin.readline

res = []

def sol():
    curInput = int(input())
    res = []
    for f in range(1, curInput - 1):
        for s in range(f + 1 , curInput) :
            if f + s == curInput :
                cur = f" {f} {s}"
                res.append(cur)
    curRes = ",".join(res)
    print(f"Pairs for {curInput}:{curRes}", )
for _ in range(int(input())):
    sol()