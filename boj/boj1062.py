import sys
input = sys.stdin.readline

alphabet = list(map(str, "abcdefghijklmnopqrstuvwxyz"))
t = list(map(str, "antatica"))
ad = {}
for a in alphabet :
    ad[a] = False
for a in t :
    ad[a] = True

count = len(list(filter(lambda x: x == True, ad.values())))
nt = list(filter (lambda x: x[1] == False, ad.items()))
nt = list(map(lambda x: x[0], nt))
N, M = list(map(int, input().split()))
words = list(map(lambda x: input().strip(), range(N)))

if M < count :
    print(0)
    exit(0)
def combination(board: list, boardCount: int) :
    cur = []
    res = []
    board = board[:]
    curInd = 0
    def dfs(depth) :
        nonlocal curInd
        if depth == boardCount :
            res.append(cur[:])
            return 
        for ind in range(curInd, len(board)) :
            curE = board[ind]
            curInd = ind + 1
            cur.append(curE)
            dfs(depth + 1)
            curInd = ind
            cur.pop()

    dfs(0)
    return res
curRes = 0
def check(cur) :
    for val in cur :
        if ad[val] == False:
            return False
    return True
for items in combination(nt, M - count) :
    for item in items :
        ad[item] = True
    cur = len(list(filter(lambda x: check(x), words)))
    curRes = max(cur, curRes)
    for item in items :
        ad[item] = False
print(curRes)