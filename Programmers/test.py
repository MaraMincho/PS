
s = [2, 3, 5, 1, 4, 3]

ans = []
def dfs() :
    if not s :
        if sum(ans) == 0:
            print(ans[::-1])
        return
    
    cur = s.pop()
    ans.append(cur)
    dfs()
    ans[-1] = -ans[-1]
    dfs()
    ans.pop()
    s.append(cur)

print(3 + 14 + 12 + 10 + 6 + 8 + 2)