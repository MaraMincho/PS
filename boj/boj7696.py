import sys

def sol():

    nums = []
    tasks = list(map(lambda _: False, range(10)))
    cur = ""
    def dfs(curDepth, targetDepth):
        nonlocal cur
        if curDepth == targetDepth :
            nums.append(cur)
            return 
        for ind in range(10) :
            if curDepth == 0 and ind == 0 or tasks[ind]:
                continue
            cur += str(ind)
            tasks[ind] = True
            dfs(curDepth + 1, targetDepth)
            tasks[ind] = False
            cur = cur[:-1]
    
    targetDepth = 1
    while len(nums) < 1_000_000 :
        dfs(0, targetDepth)
        targetDepth += 1
    res = []
    while True:
        n = int(sys.stdin.readline())
        if n == 0 :
            break
        res.append(nums[n - 1])
    print("\n".join(res))

import sys

def sol():
    nums = []
    cur = 1
    while len(nums) < 1000000 :
        curs = str(cur)
        if len(curs) == len(set(curs)):
            nums.append(str(cur))
        cur += 1

    res = []
    while True:
        n = int(sys.stdin.readline())
        if n == 0 :
            break
        res.append(nums[n - 1])
    print("\n".join(res))

sol()