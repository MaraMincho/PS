import sys

input = sys.stdin.readline

def fold(s):
    l = len(s) // 2
    h = s[:l] + [s[l]]
    t =  s[l:][::-1]
    return list(map(lambda ind: t[ind] + h[ind], range(len(t))))

def sol():
    input()
    s = list(map(int, input().split()))
    while len(s) != 2:
        s = fold(s)
    return "Alice" if s[0] > s[1] else "Bob"

for ind in range(int(input())):
    print(f'Case #{ind + 1}: {sol()}')
