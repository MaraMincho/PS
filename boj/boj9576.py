import sys
sys.setrecursionlimit(10_000_000)
input = sys.stdin.readline

def dfs(person) :
    curStart, curEnd = people[person]
    for ind in range(curStart, curEnd + 1) :
        if visited[ind] :
            continue
        visited[ind] = True
        if (books[ind] == 0 or dfs(books[ind])) :
            books[ind] = person
            return True
    return False

for _ in range(int(input())):
    n, m = map(int, input().split())
    books = [0] * (n + 1)
    people = [0]
    cnt = 0

    for _ in range(m):
        start, end = map(int, input().split())
        people.append((start, end))

    for i in range(1, m + 1):
        visited = [False] * (n + 1)
        if dfs(i):
            cnt += 1
    print(cnt)