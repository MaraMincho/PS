import sys
input = sys.stdin.readline

s = list(map(lambda _: False, range(0, 21)))
for _ in range(int(input())) :
    c = input().split()
    if c[0] == "add" :
        s[int(c[1])] = True
    elif c[0] == "check" :
        print("1" if s[int(c[1])] else "0") 
    elif c[0] == "remove" :
        s[int(c[1])] = False
    elif c[0] == "toggle":
        s[int(c[1])] = not s[int(c[1])] 
    elif c[0] == "all":
        s = list(map(lambda _ : True, range(0, 21)))
    else :
        s = list(map(lambda _ : False, range(0, 21)))
