### boj22859
## <div> </div>안에 또다른 <div>태그는 없음
## <p>태그 안에 다른 태그 존재 가능(<i>, </i>)
## stack을 활용해서 특정 태그에 대한 로직을 진행하면서 풀기
## 1. main 태그 확인
## 2. div태그 안에 존재하는 title확인
## 3. <p>태그 안에 존재하는 문장들 확인


import sys
import re

input = sys.stdin.readline
html = input().strip()
html = html[6:-7]
divTagRegex = r'<div (.*?">.*?)<\/div>'

titleCount = 0
res = []

targets = re.findall(divTagRegex, html)
for divString in targets:
    titleRe = r'.*title="(.*)".*'
    curTitle = re.search(titleRe, divString).group(1)
    res.append(f"title : {curTitle}")
    removeDivTagRe = r'<div .*">(.*)<\/div>'
    pTagRegex = r'<p>(.*?)<\/p>'
    divContent = re.findall(pTagRegex, divString)
    removeRegex = r'<.*?>'
    for cur in divContent :
        tempRes = re.sub(removeRegex, "", cur)
        res.append(re.sub(' +', ' ', tempRes))
print("\n".join(res))