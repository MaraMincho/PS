
import sys
import functools

(x, y) = list(map(int, sys.stdin.readline().split()))

xl = list(map(int, range(x - y + 1, x + 1)))
xl.reverse()
yl = list(map(int, range(1, y + 1)))
yl = yl[1:]

for ind in range(len(xl)) :
    curX = xl[ind]
    if yl == [] :
        break
    curY = yl.pop()
    if curX % curY == 0:
        xl[ind] = curX // curY
    else :
        yl.append(curY)

print(functools.reduce(lambda x, y: x * y, xl, 1))
