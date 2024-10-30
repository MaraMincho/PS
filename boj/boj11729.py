import sys
input = sys.stdin.readline

n = int(input())

res = []

def move(ind, start, to) :
    res.append(f"{start} {to}")

def hanoi(n, start, to, via) :
    if n == 1 :
        move(1, start, to)
    else :
        hanoi(n - 1, start, via, to)
        move(n, start, to)
        hanoi(n - 1, via, to, start)
hanoi(n, 1, 3, 2)
print(len(res))
print("\n".join(res))