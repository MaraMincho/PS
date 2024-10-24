def sol() -> str:
    nums, c = input().split()
    maxVal = int(nums[:])
    nums = list(map(lambda x: x, nums))
    c = int(c)
    visited = set()
    def dfs(depth: int) :
        nonlocal nums, c, maxVal, visited
        if c == depth :
            curVal = int("".join(nums))
            maxVal = max(maxVal, curVal)
            return
        elif (depth, tuple(nums)) in visited:
            return
        visited.add((depth, tuple(nums)))
        for curInd in range(len(nums)) :
            for nextInd in range(curInd + 1, len(nums)) :
                nums[curInd], nums[nextInd] = nums[nextInd], nums[curInd]
                dfs(depth + 1)
                nums[curInd], nums[nextInd] = nums[nextInd], nums[curInd]
    dfs(0)
    return maxVal
print(sol())