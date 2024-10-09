import sys
import collections

sys.setrecursionlimit(1000000000)
input = sys.stdin.readline

## n파일의 갯수, m 폴더의 갯수
(n, m) = list(map(int, input().split()))
forderAndFiles = collections.defaultdict(list)
forderAndForders = collections.defaultdict(list)

for _ in range(n + m) :
    (root, child, type) = input().split()
    if type == "0" :
        forderAndFiles[root] = forderAndFiles[root] + [child]
    else :
        forderAndForders[root] = forderAndForders[root] + [child]


res = collections.defaultdict(list)
def dfs(root: int):
    global forderAndFiles, forderAndForders, res
    if res[root] != [] :
        return
    tempRes = []
    for childFolder in forderAndForders[root]:
        if res[childFolder] == []:
            dfs(childFolder)
        list(map(lambda x: tempRes.append(x), res[childFolder]))
    list(map(lambda x: tempRes.append(x), forderAndFiles[root]))
    res[root] = tempRes
q = int(input())
qs = []

dfs("main")
for ind in range(q) :
    curInput = list(map(str, input().strip().split("/")))
    curFiles = res[curInput[-1]]
    qs.append(f"{len(list(set(curFiles)))} {len(curFiles)}")
print("\n".join(qs))