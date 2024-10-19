import sys
input = sys.stdin.readline

n = int(input())
words = []
originalWords = []
for ind in range(n):
    word = input().strip()
    words.append([word, ind])
    originalWords.append(word)

words.sort()

maxPrefixLen = 0
resultInd = sys.maxsize 

for i in range(n - 1):
    word1, idx1 = words[i]
    word2, idx2 = words[i + 1]
    
    commonPrefixLen = 0
    while commonPrefixLen < len(word1) and commonPrefixLen < len(word2) and word1[commonPrefixLen] == word2[commonPrefixLen]:
        commonPrefixLen += 1

    if commonPrefixLen > maxPrefixLen:
        maxPrefixLen = commonPrefixLen
        resultInd = min([idx1, idx2])

    elif commonPrefixLen == maxPrefixLen:
        minIdxVal = min([idx1, idx2])
        # 입력된 순서로 더 앞선 단어를 우선적으로 선택
        if minIdxVal < resultInd:
            resultInd = minIdxVal

# 결과 출력
targetPrefix = originalWords[resultInd][:maxPrefixLen]
resFlga = 0
for word in originalWords:
    if word[:maxPrefixLen] == targetPrefix:
        print(word)
        resFlga += 1
        if resFlga == 2 :
            break