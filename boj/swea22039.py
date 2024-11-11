board = ["impossible","BA", "BBA", "impossible", "BABBA"]

while len(board) < 100:
    if board[-3] == "impossible" :
        board.append("impossible")
        continue
    board.append(board[-3] + "BBA")

for _ in range(int(input())) :
    print(board[int(input()) - 1])