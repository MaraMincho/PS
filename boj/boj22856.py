import sys
sys.setrecursionlimit(1000000)

input = sys.stdin.readline

### [int: (int, int)]
tree = {}

n = int(input())
for _ in range(n):
    (root, left, right) = list(map(int, input().split()))
    tree[root] = (left, right)

res = 0

resFlag = False
visitedCount = 0


def dfs(root: int):
    global res, visited, tree, resFlag, treeLastNode, visitedCount

    left, right = tree[root]
    
    if left != -1 :
        res += 1
        dfs(left)
        if resFlag == False:
            res += 1
    visitedCount += 1
    if visitedCount == n :
        resFlag = True
    if right != -1 :
        res += 1
        dfs(right)
        if resFlag == False:
            res += 1
        
dfs(1)
print(res)