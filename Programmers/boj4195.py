import sys
input = sys.stdin.readline

def sol():
    u = {}
    uv = {}
    def find(s) :
        if u[s] == s :
            return s
        return find(u[s])
    
    def merge(a, b) :
        ap, bp = find(a), find(b)
        if ap == bp :
            return uv[ap]
        if bp < ap :
            u[b] = ap
            u[bp] = ap
            uv[ap] += uv[bp]
            return uv[ap]
        else :
            u[a] = bp
            u[ap] = bp
            uv[bp] += uv[ap]
            return uv[bp]
    
    for _ in range(int(input())) :
        f1, f2 = input().split()
        
        for val in [f1, f2]:
            if val not in u :
                u[val] = val
                uv[val] = 1
        print(merge(f1, f2))

for _ in range(int(input())) :
    sol()