import sys

while True:
    lines = list(map(int, input().split()))
    lines.sort()
    lines = list(map(lambda x: x * x, lines))
    if sum(lines) == 0 :
        break
    print("right" if lines[0] + lines[1] == lines[2] else "wrong")