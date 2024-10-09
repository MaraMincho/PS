import collections
import sys

q = collections.deque()

for _ in range(int(sys.stdin.readline())):
    cur = sys.stdin.readline().split()
    
    if cur[0] == "push" :
        q.append(cur[1])
        
    elif cur[0] == "pop":
        if not q :
            print("-1")
            continue
        print(q.popleft())
        
    elif cur[0] == "size":
        print(len(q))
        
    elif cur[0] == "empty" :
        print("1" if not q else "0")
    
    elif cur[0] == "front":
        if not q:
            print("-1")
        else :
            print(q[0])
    elif cur[0] == "back":
        if not q :
            print("-1")
        else:
            print(q[-1])
    
