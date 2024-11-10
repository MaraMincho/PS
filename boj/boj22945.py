import sys
input = sys.stdin.readline

N = int(input())
board = list(map(int, input().split()))

left, right = 0, N - 1
cur = 0

while left < right :
    tempCur = (right - left - 1) * min(board[left], board[right])
    cur = max(cur, tempCur)
    if board[left] < board[right] :
        left += 1
    else :
        right -= 1
print(cur)