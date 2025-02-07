
number = 0
while number < 30:
    number += 1 
    numberToStr = str(number) 
    flag = True 
    for cur in numberToStr: 
        curToInt = int(cur) 
        if not curToInt == 0 and curToInt % 3 == 0:
            flag = False
            break

    if flag == True :
        print(number)
    else:
        print(number, "짝")
        

 # 3으로 나눴을때 어떠한 규칙도 찾을 수없다.
    # 12 / 3 -> 4... 0 ? -> 거짓
    # 3 / 3 -> 1 ... 0 ? -> 참
    # 13 / 3 -> 4 ... 1 ? -> 참
    # 14 / 3 -> 4 ... 2 ? -> 거짓
    # 15 / 3 -> 5 ... 0 ? -> 거짓
    
    # 숫자를 3으로 나눌거임. 근데 나누는 것은 각 자리 숫자이여야만 함.
    # 각 자리의 숫자를 나눠서 3으로 나누어떨어지는지 확인
    # 나누어떨어진다? -> 3,6,9수 (0을 제외한 조건이 붙습니다.)
    
    
    # 3 -> "3" -> 3 / 3 = 1 ... 0 (참)
    # 13  -> "1", "3" -> 1 / 3 = 0 ... 1, 3 / 3 = 1...0 (참)
    # 14 -> "1", "4" -> 1 / 3 = 0 ... 1, 4 / 3 = 1 ... 1(거짓)
    # 15 -> "1", "5"
    # 16 -> "1", "6"
    # 10 -> "1", "0" -> 1 / 3 = 0 ... 1, 0 / 3 = 0 ... 0

# 어떠한 int형 숫자를 받습니다.
def d(val: int) :
    # int형 숫자를 다시 str으로 변환합니다.
    numberToStr = str(val) # 10 -> "10"
    
    # "10" -> ["1", "0"]
    # cur = "1"
    # curToInt = 1 
    for curStr in numberToStr: 
        curToInt = int(curStr) 
        
        if not curToInt == 0 and curToInt % 3 == 0:
            return True
    return False