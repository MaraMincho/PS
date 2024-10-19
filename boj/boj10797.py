n = int(input())
arrs = list(map(int, input().split()))
print(len(list(filter(lambda x: x== n, arrs))))