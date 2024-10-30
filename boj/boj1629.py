import sys
input = sys.stdin.readline

x, y, z = list(map(int, input().split()))

def sol(x, y, z) :
    if y == 1 :
        return x % z
    else :
        cur = sol(x, y // 2, z)
        if y % 2 == 0 :
            return (cur % z) * (cur % z) % z
        else :
            return (cur % z) * (cur % z) * (x % z) % z
print(sol(x, y, z))