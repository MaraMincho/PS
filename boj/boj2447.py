import sys
input = sys.stdin.readline

N = int(input())

def re(n: int) :
    if n == 3 :
        return ["***", "* *", "***"]
    else :
        third = n // 3
        thirdTopAndBottom = re(third)
        topAndBottom = list(map(lambda x: x * 3, thirdTopAndBottom))
        emptyMid = [" " * third  for _ in range(third)]
        mid = list(map(lambda ind: thirdTopAndBottom[ind] + emptyMid[ind] + thirdTopAndBottom[ind], range(third)))
        return topAndBottom[:] + mid + topAndBottom[:]

print("\n".join(re(N)))