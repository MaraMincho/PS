import sys

input = sys.stdin.readline
n = int(input())

start = 1
end = n
s = []
while len(s) != n:
    if len(s) % 2 == 0 :
        s.append(end)
        end -= 1
    else :
        s.append(start)
        start += 1
print(*s)