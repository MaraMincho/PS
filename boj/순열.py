

curStr = str(input())
leftInd = int(input())
rightInd = int(input())
n = int(input())

dicts = {"1" : "132", "2": "211", "3":"232"}

for _ in range(n):
    prev = ""
    
    for ind in range(len(curStr)) :
        prev += dicts[curStr[ind]]
    curStr = prev

fc, sc, tc = 0, 0, 0
for ind in range(leftInd, rightInd + 1) :
    if curStr[ind] == "1" :
        fc += 1
    elif curStr[ind] == "2" :
        sc += 1
    else :
        tc += 1

print(f"{fc} {sc} {tc}")

