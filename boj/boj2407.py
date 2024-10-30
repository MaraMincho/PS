import sys
input = sys.stdin.readline

n, m = list(map(int, input().split()))

pascalTriangle = [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]
curInd = 4
while curInd <= n :
    cur = []
    for ind in range(curInd - 1) :
        cur.append(pascalTriangle[-1][ind] + pascalTriangle[-1][ind + 1])
    pascalTriangle.append([1] + cur + [1])
    curInd += 1
print(pascalTriangle[n][m])