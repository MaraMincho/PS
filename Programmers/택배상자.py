def solution(order):
    originalOrder = order[:]
    answer = 0
    other = []
    cur = list(map(lambda x: x, range(1, len(order) + 1)))[::-1]
    
    order = order[::-1]
    while cur :
        last = cur.pop()
        if last == order[-1] :
            order.pop()
            
            while other and order and other[-1] == order[-1] :
                order.pop()
                other.pop()
            continue
        other.append(last)
    return len(originalOrder) - len(cur + other)