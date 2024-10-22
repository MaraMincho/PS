import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

dividVal = 1_000_000_007
sumArr = [arr[0]]
res = 0
for ele in arr[1:]:
    res += (sumArr[-1] * ele)
    res %= dividVal
    cur = (sumArr[-1] + ele) % dividVal
    sumArr.append(cur)
print(res)