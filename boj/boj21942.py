import sys
import collections
input = sys.stdin.readline

N, L, F = input().split()
N, F = tuple(map(int, [N, F]))
lentalMinutes = int(L[:3]) * 60 * 24 + int(L[4:6]) * 60 + int(L[7:])
monthAndDay = {1: 0, 2: 31, 3: 28, 4: 31, 5: 30, 6: 31, 7: 30, 8: 31, 9: 31, 10: 30, 11: 31, 12: 30}
for ind in range(2, 13) :
    monthAndDay[ind] += monthAndDay[ind - 1]

book = {}
answer = collections.defaultdict(int)

def makeKey(product, user) :
    return product + "-"  + user

def setProduct(month, day, time, product, user) :
    global book
    book[makeKey(product, user)] = (month, day, time)

def getMinutes(month, day, time) -> int :
    global monthAndDay
    hour, minutes = int(time[:2]), int(time[3:])
    return monthAndDay[month] * 24 * 60 + day * 24 * 60 + hour * 60 + minutes
    
def compareProduct(month, day, time, product, user):
    global book
    prevMonth, prevDay, prevTime = book[makeKey(product, user)]
    prevMinutes = getMinutes(prevMonth, prevDay, prevTime)
    curMinutes = getMinutes(month, day, time)
    subMinutes = curMinutes - prevMinutes
    if lentalMinutes < subMinutes:
        answer[user] += (subMinutes - lentalMinutes) * F
    
for _ in range(N):
    yearMonthDay, time, product, user = input().split()
    (_, month, day) = list(map(int, yearMonthDay.split(sep="-")))
    if book.get(makeKey(product=product, user=user)) == None:
        setProduct(month=month, day=day, time=time, product=product, user=user)
    else :
        compareProduct(month=month, day=day, time=time, product=product, user=user)
        book.pop(makeKey(product=product, user=user))

if answer :
    answer = sorted(answer.items(), key= lambda x: x[0])
    [ print(x[0], x[1]) for x in answer]
else :
    print("-1")