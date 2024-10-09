import sys
import re

view_regex = r"case \.view\((.*)\)"
async_regex = r"case \.async\((.*)\)"
inner_regex = r"case \.inner\((.*)\)"
scope_regex = r"case \.scope\((.*)\)"

lines = sys.stdin.readlines()

view_cases = []
async_cases = []
inner_cases = []
scope_cases = []


ind = 0
max_line = len(lines)
not_case_regex = r"[ ]*case.*|[ ]*}[ ]*"
while ind < max_line :
    line = lines[ind]
    curStrings = []
    view_match = re.search(view_regex, line)
    async_match = re.search(async_regex, line)
    inner_match = re.search(inner_regex, line)
    scope_match = re.search(scope_regex, line)
    if view_match:
        curStrings.append(".case" + view_match.group(1) + "\n")
    elif async_match:
        curStrings.append(".case" + async_match.group(1)+ "\n")
    elif inner_match:
        curStrings.append(".case" + inner_match.group(1)+ "\n")
    elif scope_match:
        curStrings.append(".case" + scope_match.group(1)+ "\n")
    
    nextLineInd = ind + 1
    while ind < max_line :
        nextLine = lines[nextLineInd]
        if re.search(not_case_regex, nextLine):
            ind = nextLineInd - 1
            break
        else :
            curStrings.append(nextLine)
            nextLineInd + 1
    
    ind += 1
    if view_match:
        view_cases.append("".join(curStrings))
    if async_match:
        async_cases.append("".join(curStrings))
    if inner_match:
        inner_cases.append("".join(curStrings))
    if scope_match:
        scope_cases.append("".join(curStrings))



print("View Cases:", view_cases)
print("Async Cases:", async_cases)
print("Inner Cases:", inner_cases)
print("Scope Cases:", scope_cases)