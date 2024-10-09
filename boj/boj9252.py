s1 = list(map(str, input().strip()))
s2 = list(map(str, input().strip()))

dp = list(map(lambda _ : [0] * len(s1), range(len(s2))))
dps = list(map(lambda _ : [""] * len(s1), range(len(s2))))

dp[0][0] = 1 if s1[0] == s2[0] else 0
dps[0][0] = s1[0] if s1[0] == s2[0] else ""

# 첫 번째 행 채우기
for col in range(1, len(s1)) :
    cur = 1 if s1[col] == s2[0] else 0
    curs = s1[col] if s1[col] == s2[0] else ""
    dp[0][col] = max(dp[0][col - 1], cur)
    if dp[0][col - 1] < cur :
        dps[0][col] = curs
    else :
        dps[0][col] = dps[0][col - 1]

# 첫 번째 열 채우기
for row in range(1, len(s2)) :
    cur = 1 if s1[0] == s2[row] else 0 
    curs = s2[row] if s1[0] == s2[row] else ""
    dp[row][0] = max(dp[row - 1][0], cur)
    if dp[row - 1][0] < cur :
        dps[row][0] = curs
    else :
        dps[row][0] = dps[row - 1][0]

# 나머지 dp와 dps 채우기
for row in range(1, len(s2)) : 
    for col in range(1, len(s1)):
        w = 1 if s1[col] == s2[row] else 0
        ws = s1[col] if s1[col] == s2[row] else ""

        # 세 가지 방향에서 최댓값 선택
        if dp[row - 1][col] > dp[row][col - 1]:
            if dp[row - 1][col] > dp[row - 1][col - 1] + w:
                dp[row][col] = dp[row - 1][col]
                dps[row][col] = dps[row - 1][col]
            else:
                dp[row][col] = dp[row - 1][col - 1] + w
                dps[row][col] = dps[row - 1][col - 1] + ws
        else:
            if dp[row][col - 1] > dp[row - 1][col - 1] + w:
                dp[row][col] = dp[row][col - 1]
                dps[row][col] = dps[row][col - 1]
            else:
                dp[row][col] = dp[row - 1][col - 1] + w
                dps[row][col] = dps[row - 1][col - 1] + ws

# 결과 추출
colCount = len(s1) - 1
lastLine = list(map(lambda x: dps[x][colCount], range(len(s2))))
ans = max(lastLine, key= lambda x: len(x))

# 결과 출력
print(len(ans))
if len(ans) != 0:
    print(ans)