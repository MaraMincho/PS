import sys
import itertools
input = sys.stdin.readline

board = list(map(lambda _: True, range(100001)))
maxValue = 100001
p = []
t = []
flag = True
for ind in range(2, maxValue // 2):
    if board[ind] == False :
        continue
    temp = ind + ind
    
    while temp < maxValue :
        board[temp] = False
        temp += ind
    
    for x in p:
        m = x * ind
        if m > maxValue:
            break
        t.append(m)
        
    
    p.append(ind)
t.sort()

def check(val):
    start, end = 0, len(t)
    while start < end:
        mid = (start + end) // 2
        cur = t[mid]
        if cur < val :
            start = mid + 1
        else:
            end = mid
    print(t[start])
for _ in range(int(input())):
    check(int(input()))