cur = list(map(int, input().split()))
target = list(range(1, 8 + 1))
if cur == target:
    print("ascending")
elif cur == target[::-1]:
    print("descending")
else:
    print("mixed")
