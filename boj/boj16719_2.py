import sys
input = sys.stdin.readline

targetString = input().strip()
res = []
visited = [""] * len(targetString)
def find(startInd, prevString) :
    if not prevString:
        return
    minVal = min(prevString)
    minIndex = prevString.index(minVal)
    visited[minIndex + startInd] = minVal
    res.append("".join(visited))
    find(startInd + minIndex + 1, prevString[minIndex + 1:])
    find(startInd, prevString[: minIndex])
    
find(0, targetString)
print("\n".join(res))