import sys

input = sys.stdin.readline

(C, N) = list(map(int, input().split()))

cities = []
maxPeople = C
for _ in range(N):  
    (b, p) = list(map(int, input().split()))
    if (C % p) != 0 :
        maxPeople = max(( C // p ) * p + p, maxPeople)
    cities.append([b, p])
cities = sorted(cities, key = lambda x: [x[0], x[1]])

## index는 person, 값은 budget 
budgets = [sys.maxsize for _ in range(maxPeople + 1)]

budgets[0] = 0
for city in cities :
    (b, p) = (city[0], city[1])
    for cur in range(maxPeople + 1):
        if cur < p :
            continue
        if budgets[cur - p] + b < budgets[cur] :
            budgets[cur] = budgets[cur - p] + b
print(min(budgets[C:]))