import sys
input = sys.stdin.readline

def sol() :
    N = int(input())
    board = list(map(int, input().split()))
    board.sort()
    for _ in range(N):
        board[0] += 1
        board[-1] -= 1
        board.sort()
    print(board[-1] - board[0])

for ind in range(10):
    print(f"#{ind+1} ", end= "")
    sol()