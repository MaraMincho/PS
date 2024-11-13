import sys

input = sys.stdin.readline
dp = [1, 3, 7]
def move(start, end) :
    print(start, end)

def hanoi(start, mid, end, num) :
    if num == 1 :
        move(start, end)
        return
    hanoi(start, end, mid, num - 1)
    move(start, end)
    hanoi(mid, start, end, num - 1)

def sol() :
    N = int(input())
    while len(dp) < N :
        dp.append(dp[-1] + dp[-1] + 1)
    print(dp[N - 1])
    if N <= 20 :
        hanoi(1, 2, 3, N)
sol()