def solution(arr):
    d = {1: 0, 0: 0}
    def find(r0, c0, r1, c1) :
        nonlocal arr
        first = arr[r0][c0]
        if r0 == r1 :
            d[first] += 1
            return
        flag = True
        for r in range(r0, r1):
            if not flag :
                break
            for c in range(c0, c1) :
                if first != arr[r][c] :
                    flag = False
                    break
        if not flag :
            mr, mc = (r1 + r0) // 2, (c1 + c0) // 2
            find(r0, c0, mr, mc)
            find(mr, c0, r1, mc)
            find(r0, mc, mr, c1)
            find(mr, mc, r1, c1)
        else :
            d[first] += 1
        
    find(0,0, len(arr) , len(arr))
    return [d[0], d[1]]