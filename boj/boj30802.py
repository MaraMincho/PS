import sys
import math
input = sys.stdin.readline

nums = int(input())
shirts = list(map(int, input().split()))
T, P = list(map(int, input().split()))

print(sum(list(map(lambda x: math.ceil(x / T), shirts))))
print(nums // P, nums % P)