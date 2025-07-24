import sys
input = sys.stdin.readline

def s():
    m, md, wd = list(map(int, input().split()))
    ans = 1
    cd = 1
    while cd < m * md:
        if cd % wd == 0:
            ans += 1
        elif cd % md == 0:
            ans += 1
        cd += 1
    return ans

for i in range(int(input())):
    print(f"Case #{i+1}: {s()}")