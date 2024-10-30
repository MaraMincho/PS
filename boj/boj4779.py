import sys

cur = sys.stdin.readlines()

visited = {1: "-"}
def ka(cur) -> str:
    if visited.get(cur) :
        return visited[cur]
    third = cur // 3
    curVisited = ka(third) + " " * third + ka(third)
    visited[cur] = curVisited
    return curVisited
res = []
for val in cur :
    val = val.replace("\n", "")
    val = int(val)
    res.append(ka(3 ** val))
print("\n".join(res))