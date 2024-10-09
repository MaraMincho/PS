import itertools
import sys

def sol(val: int) :
    curList = list(map(lambda x: str(x + 1), range(val)))
    
    bridgeList = ["", "+", "-"]
    bridge = list(map(lambda x: 0, range(val - 1)))
    
    for p in itertools.product(bridgeList, repeat = val - 1):
        prev = curList[0]
        for ind in range(len(p)) :
            curP = p[ind]
            prev += curP + curList[ind + 1]
        # print(eval(prev), prev)
        if eval(prev) == 0 :
            curValue = ""
            for ind in range(val):
                curValue += curList[ind]
                if ind < val - 1 :
                    curValue += " " if p[ind] == "" else p[ind]
            print(curValue)

for _ in range(int(sys.stdin.readline())) :
    sol(int(sys.stdin.readline()))
    print()