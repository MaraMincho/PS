def solution(users, emoticons):
    discounts = [10, 20, 30, 40]
    
    curDiscount = []
    targetDepth = len(emoticons)
    targetUsers = list(map(lambda x: x + [x[1]], users))
    
    def currentValue() :
        nonlocal targetUsers, curDiscount, emoticons
        currentUser = list(map(lambda x: x[:], targetUsers))
        for (emoticion, discount) in zip(emoticons, curDiscount) :
            curVal = int(emoticion * (1 - discount / 100))
            for ind, (ud, uo, ur) in enumerate(currentUser) :
                if ud <= discount :
                    currentUser[ind] = [ud, uo, ur - curVal]    
        plusCount = len(list(filter(lambda x: x[2] <= 0, currentUser)))
        
        resB = sum(list(map(lambda x: x[1] - x[2] if x[2] > 0 else 0, currentUser)))
        print(currentUser, curDiscount, (plusCount, resB))
        return plusCount, resB
    
    resPlusCount, resPrice = 0, 0 
    def dfs(depth) :
        nonlocal targetDepth, discounts, resPlusCount, resPrice
        if depth == targetDepth :
            tpc, tp = currentValue()
            print(tpc, tp)
            if resPlusCount < tpc  :
                resPlusCount = tpc
                resPrice = tp
            elif tpc == resPlusCount and tp > resPrice:
                resPrice = tp
            return 
        for discount in discounts :
            curDiscount.append(discount)
            dfs(depth + 1)
            curDiscount.pop()
    dfs(0)
    
    return [resPlusCount, resPrice]

print(solution([[40, 10000], [25, 10000]],	[7000, 9000]))
