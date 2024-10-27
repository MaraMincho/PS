import sys
sys.setrecursionlimit(10_000_000)
input = sys.stdin.readline

peopleCount, taskCount = list(map(int, input().split()))

tasks = [[0]] + [list(map(int, input().split()))[1:] for _ in range(peopleCount)]
    
assigned_tasks = [0] + [-1] * taskCount
visited = []
def dfs(person) :
    for ind in tasks[person] :
        if visited[ind] :
            continue
        visited[ind] = True
        
        if assigned_tasks[ind] == -1 or dfs(assigned_tasks[ind]) :
            assigned_tasks[ind] = person
            return True
    return False
res = 0
for ind in range(1, peopleCount + 1) :
    visited = [False] * (taskCount + 1)
    if dfs(ind) :
       res += 1
print(res)