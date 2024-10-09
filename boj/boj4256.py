
import sys
def sol() :
    n = int(sys.stdin.readline())
    preOrder = list(map(int, sys.stdin.readline().split()))
    inOrder = list(map(int, sys.stdin.readline().split()))
    
    eStack = []
    ind = 0
    trees = {}
    prevNodes = []
    for pEle in preOrder :
        iEle = inOrder[ind]
        if pEle != iEle :
            eStack.append(pEle)
            continue
        
        while eStack != [] and eStack[-1] == iEle[ind] :
            ind += 1
        
