import sys
import re

html = sys.stdin.readlines()
html = "".join(html)
html = re.sub(r'\n', " ", html)

hrContent = "--------------------------------------------------------------------------------"
html = html.split("\n")
res = []
for temp in html:
    tempRes = []
    tempCount = 0
    splited = temp.split(sep=" ")
    for cur in splited:
        if not cur :
            continue
        if cur == "<br>":
            merged = " ".join(tempRes)
            res.append(merged)
            tempRes = []
            tempCount = 0
        elif cur == "<hr>" :
            merged = " ".join(tempRes)
            if merged != "" :
                res.append(merged)
            res.append(hrContent)
            tempRes = []
            tempCount = 0
        elif tempCount + len(cur) + len(tempRes) - 1 > 80 :
            tempCount = 0
            merged = " ".join(tempRes)
            res.append(merged)
            tempRes = [cur]
        else :
            tempCount += len(cur)
            tempRes.append(cur)
    if tempRes :
        merged = " ".join(tempRes)
        res.append(merged)
print("\n".join(res))