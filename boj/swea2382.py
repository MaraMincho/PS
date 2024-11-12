import sys
input = sys.stdin.readline

def sol() :
    dirs = {1: (-1, 0), 4: (0, 1), 3: (0, -1), 2: (1, 0)}
    N, M, K = list(map(int, input().split()))
    # (row, col, coumt, dir)
    bugs = []
    for _ in range(K) :
        bugs.append(tuple(map(int, input().split())))
        
    spin = {1: 2, 2: 1, 3: 4, 4: 3}
    def next() :
        nonlocal bugs
        board = {}
        for bug in bugs :
            (row, col, count, dir) = bug
            dirV = dirs[dir]
            nextRow, nextCol = dirV[0] + row, dirV[1] + col
            board[(nextRow, nextCol)] = board.get((nextRow, nextCol), []) + [(count, dir)]
        currentBugs = []
        for key, value in board.items() :
            row, col = key
            maxdValue = max(value)
            currentDir = maxdValue[1]
            currentCount = sum(list(map(lambda x: x[0], value)))
            
            if row == 0 or row == N -1 :
                currentDir = spin[currentDir]
                currentCount = currentCount // 2
            elif col == 0 or col == N - 1:
                currentDir = spin[currentDir]
                currentCount = currentCount // 2
            currentBugs.append( (row, col, currentCount, currentDir) )
        bugs = currentBugs  
    
    for _ in range(M):
        next()
    
    return sum(list(map(lambda x: x[2], bugs)))

for ind in range(int(input())) :
    print(f"#{ind + 1} {sol()}")