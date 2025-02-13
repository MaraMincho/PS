
# Scanf -> 표준 입출력을 받아드린다. 

# myString = "asdf"
# print(myString, type(myString))
# print(int(myString), type(int(myString)))

# firstInt = input()
# secondInt = input() 
# print(int(firstInt), "+", int(secondInt), int(firstInt) + int(secondInt))

# a = input() -> "1"
# 2
# 3 4 -> a = 3, b = 4
# 3 4 - > ['3', '4']
# "3 4"
# twoInts = input()
# print("\"", twoInts, "\"")
# w = twoInts.split(sep=" ")

# for index in range(len(w)) :
#     w[index] = int(w[index])

# for val in w :
#     print("value, ", val, type(val))

    
# print(w) # ['30', '40']
# print(w[0] + w[1])

# myIntList = []
# for value in w : # ['30', '40']
#     myIntList.append(int(value))
# print("myIntList[0] + myIntList[1] = ", myIntList[0] + myIntList[1])

# Current값의 후보는? -> 

# 12345 -> ["1", "2", "3", "4", "5"]


# "3015" -> ["3", "0", "1", "5"] -> int(3) % 3 = 1...(0) 나머지가 0일경우 박수를 쳤습니다.
# qweasdf -> ['q', 'w', 'e', 'a', 's', 'd', 'f']
myString = input()
for val in myString :
    print(val)
    if int(val) != 0 and int(val) % 3 == 0 :
        print("짝")
        
# 띄어쓰기를 통해 두가지 값을 받고 두 값의 3,6,9 여부를 판단한다.
# 두 값을 더하고 더한 값의 3, 6, 9 여부를 판단한다.