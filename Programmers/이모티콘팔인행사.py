def solution(users, emoticons):
    answer = []
    
    def bs(emoticon, users):

        def cal(users, discount, emoticon):
            userCount = 0
            curPlus = 0
            for user in users:
                curValue = int(emoticon * (1 - discount / 100))
                if user[0] <= discount :
                    if user[2] - curValue <= 0 :
                        curPlus += 1
                        continue
                    userCount += 1
                    
            return (curPlus, userCount)

        
        discountTarget = list(map(lambda x: x[0], users))
        start, end = min(discountTarget), max(discountTarget)
        
        prev, prevPlus, prevDiscount = 0, 0, 0
        for discount in range(start, end + 1):
            (curPlus, curUserCount) = cal(users, discount, emoticon)
            curValue = int(emoticon * (1 - discount / 100)) * curUserCount
            print("curvalue, 디스카운트, curPlus, curUserCount", curValue, discount, curPlus, curUserCount)
            if prevPlus < curPlus :
                prev = curValue
                prevPlus = curPlus
                prevDiscount = discount                
            elif prevPlus == curPlus and prev < curValue:
                prev = curValue
                prevDiscount = discount

        return prevDiscount

    targetUsers = sorted(users, key= lambda x: [-x[1], -x[0]])
    targetUsers = list(map(lambda x: x + [x[1]], targetUsers))
    plusCount = 0
    for emoticon in sorted(emoticons)[::-1] :
        print("\n---------------------------------")
        print("현재 이모티콘 벨류", emoticon)
        print(targetUsers)
        targetDiscount = bs(emoticon, targetUsers[:])
        
        targetValue = (1 - targetDiscount/ 100)  * emoticon
        print("---------------------------------")
        print("tval:", targetValue, " discount: ", targetDiscount, "targetUsers: ", targetUsers)
        
        tempRes = []
        for ind in range(len(targetUsers)) :
            targetUserDiscount, targetUserOriginalValue, targetUserVal = targetUsers[ind]
            if targetUserDiscount <= targetDiscount :
                if targetUserVal - targetValue <= 0:
                    plusCount += 1
                    continue
                tempRes.append([targetUserDiscount, targetUserOriginalValue, targetUserVal - targetValue])
                continue
            tempRes.append(targetUsers[ind])
        targetUsers = tempRes
    
    answer = 10000 * plusCount + sum(list(map(lambda x: x[2] - x[1], targetUsers)))
        
    return answer

solution([[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]],	[1300, 1500, 1600, 4900])