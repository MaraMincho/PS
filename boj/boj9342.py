import sys
import re
input = sys.stdin.readlines

regexStr = r'\b[\w|-]+\b'
regexController = re.compile(regexStr)
curInput = input()
curInput = "".join(curInput)
fiInd = curInput.find("E-N-D")
curInput = curInput[:fiInd]
cur = regexController.findall(curInput)
print(max(cur, key= lambda x: len(x)).lower())