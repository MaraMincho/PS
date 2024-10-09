
```python

import sys
def sol():
    (x, y) = list(map(int, sys.stdin.readline().split()))

    line = [] 
    for _ in range(x):
        line.append(sys.stdin.readline())
    
    dline = []
    for _ in range(x):
        line.append(sys.stdin.readline())

    for _ in range(x):
        for curInd in range(line[x]) :
            if dline[x][curInd] == dline[x][curInd + 1] == line[x][curInd]:
                continue
            else :
                return False
    return True
print("Eyfa" if sol() else "Not Eyfa")
```