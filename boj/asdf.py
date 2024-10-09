

def sol() :
    n = []
    for _ in range(7) :
        cur = int(input())
        if cur % 2 == 1 :
            n.append(cur)
    sumVal = sum(n)
    if sumVal == 0:
        print(-1)
        return
    n.sort()
    print(sumVal)
    print(n[0])
sol()