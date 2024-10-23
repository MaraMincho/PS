import sys
input = sys.stdin.readline
n = int(input())
res = "1213"
while len(res) < n :
    for cur in ["1", "2", "3"] :
        tempInd = 2
        tempRes = res[:] + cur
        flag = False
        while tempInd <= len(tempRes):
            curRes = tempRes[len(tempRes) - tempInd:]
            leftVal = curRes[:tempInd // 2]
            rightVal = curRes[tempInd // 2 :]
            if leftVal == rightVal :
                flag = True
                break
            tempInd += 2
        if flag == False :
            res = tempRes
            break

print(res[:n])