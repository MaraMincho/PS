import itertools
def solution(n):
    answer = 0
    cur = "0" + bin(n)[2:]
    print(cur)
    startIndex = len(cur) - 1
    while startIndex > 0:
        if startIndex == len(cur) - 1 or cur[startIndex] == "1":
            startIndex -= 1
            continue
        break

    front = cur[:startIndex]
    back = cur[startIndex:]
    t = []
    for c in back :
        t.append(c)
    t.sort()
    
    prev = ""
    updateBack = back
    for val in itertools.permutations(t, len(back)) :
        if prev == back :
            updateBack = prev
            break
        prev = "".join(val)
        
    print("업데이트", back, updateBack)
    
    return answer