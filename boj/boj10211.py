import sys
input = sys.stdin.readline
def sol():
    n = int(input())
    board = list(map(int, input().split()))
    
    currentSum = 0
    bestSum = -sys.maxsize
    for num in board :
        currentSum = max(currentSum + num, num)
        bestSum = max(bestSum, currentSum)
    print(bestSum)
def sol2() :
    n = int(input())
    board = list(map(int, input().split()))
    
    currentSum = 0
    sumBoard = []
    for num in board :
        currentSum = max(currentSum + num, num)
        sumBoard.append(currentSum)
    print(max(sumBoard))
for _ in range(int(input())):
    sol2()