import sys
input = sys.stdin.readline

def box(val: int) :
    if val == 1 :
        print("#")
        return
    mid = "#" + "J" * (val - 2)  + "#"
    topAndBottom = "#" * val
    cur = [topAndBottom] + [mid] * (val - 2) + [topAndBottom]
    [print(x) for x in cur]
for _ in range(int(input())) :
    box(int(input()))
    print()
