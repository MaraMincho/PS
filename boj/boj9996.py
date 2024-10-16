import sys
import re
input = sys.stdin.readline

p = re.compile(r'^(100+1+|01)+$')
print("SUBMARINE" if p.match(input()) else "NOISE")