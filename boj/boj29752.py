import sys
input = sys.stdin.readline

input()
t = list(map(lambda x: "1" if x != "0" else "0", input().strip().split(sep=" ")))
s = "".join(t).split("0")
print(len(max(s, key=lambda x: len(x))))