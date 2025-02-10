import sys
input = sys.stdin.readline

def sol() :
    _ = input()
    res = 0
    answer = 0
    for cur in list(map(lambda x: int(x), input().split())) :
        res += 1 if cur == 1 else -1
        answer += res
    print(answer)

sol()