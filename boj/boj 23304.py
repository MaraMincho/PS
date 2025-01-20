import sys

input = sys.stdin.readline

cur = input().strip()

def sol(cur) :    
    if len(cur) == 1:
        return True
    halfLen = len(cur) // 2
    return cur == cur[::-1][:] and sol(cur[:halfLen])
    
print("AKARAKA" if sol(cur) else "IPSELENTI")