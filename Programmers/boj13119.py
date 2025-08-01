import sys
input = sys.stdin.readline

N, M, H = list(map(int, input().split()))
board = list(map(int, input().split()))
tree = list(map(lambda _: ["."] * M, range(N)))

# "#" 채우기
for i in range(M):
    cur = board[i]
    for c in range(cur):
        tree[N - 1 - c][i] = chr(35) # "#"

# "High-Way"
for i in range(M):
    tree[N - H][i] = chr(45) if tree[N - H][i] == "." else chr(42) # chr45 "-", chr42 "*"

# | 만들기
for i in range(M):
    if i % 3 == 2 and tree[N-H][i] == "-":
        for row in range(N - H  + 1, N - 1):
            if tree[row][i] == ".":
                tree[row][i] = chr(124) # chr 
                continue
            break

for x in tree:
    print("".join(x))