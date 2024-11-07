import sys
input = sys.stdin.readline

N = int(input())

q = []
board = []
for s in range(N):
    cur = list(map(int, input().split()))
    board.append(cur)
    for e in range(s + 1, N) :
        q.append((cur[e], s, e))

q = sorted(q, key= lambda x: [x[0]], reverse= True)
parents  = list(map(lambda x: x, range(N)))

def fp(cur) :
    if parents[cur] != cur :
        parents[cur] = fp(parents[cur])
    return parents[cur]
res = 0

flagCount = N - 1
while q:
    w, s, e = q.pop()
    sp, ep = fp(s), fp(e)
    if sp == ep :
        continue
    res += w
    flagCount -= 1
    if flagCount == 0 :
        break
    if sp < ep :
        parents[e] = sp
        parents[ep] = sp
    else :
        parents[s] = ep
        parents[sp] = ep
print(res)
