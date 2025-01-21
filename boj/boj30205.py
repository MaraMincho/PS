import sys
input = sys.stdin.readline


def sol() :
    N, M, P = list(map(int,input().split()))

    board = []
    for _ in range(N):
        board.append(list(map(int, input().split())))

    curP = P
    for cur in board:
        curM = len(list(filter(lambda x: x == -1, cur)))
        sortedCur = sorted(cur)
        
        for curB in sortedCur:
            if curB == 0 or curB == -1 :
                continue
            while curM > 0 and curP < curB :
                curM -= 1
                curP *= 2
            
            if curB <= curP :
                curP += curB
            else :
                return 0
        while curM > 0 :
            curM -= 1
            curP *= 2
    return 1
print(sol())
            