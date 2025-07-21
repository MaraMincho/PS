import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))

dp = A[:]  # 초기값: 자기 자신만 포함하는 경우

for i in range(n):
    for j in range(i):  # i 이전의 값들과 비교
        if A[i] < A[j]:  # 감소하는 부분 수열 조건
            dp[i] = max(dp[i], dp[j] + A[i])  # 최대 합 갱신

# print(max(dp))  # 가장 큰 감소 부분 수열의 합 출력

x = list(range(1, 9))
import itertools
a = ""

for t in itertools.combinations(x, 5) :
    cur1 = list(map(str, t))
    cur1 = int(''.join(cur1))
    
    x1 = list(filter(lambda x: not x in t, x))
    for t2 in itertools.combinations(x1, 4) :
        cur2  = int(''.join(list(map(str, t2))))
        if cur1 - cur2 == 0 :
            print(cur1, cur2)
    
