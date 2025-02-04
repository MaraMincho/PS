def solution(n, m, x, y, r, c, k):
    directions = [("d", (1, 0)), ("l", (0, -1)), ("r", (0, 1)), ("u", (-1, 0))]
    start, end = (x, y), (r, c)

    def distance(p1, p2):
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

    def is_valid(pos):
        return 1 <= pos[0] <= n and 1 <= pos[1] <= m

    min_steps = distance(start, end)

    # Impossible 조건 체크
    if k < min_steps or (k - min_steps) % 2 == 1:
        return "impossible"

    extra_moves = (k - min_steps) // 2
    current = start
    path = ""

    def move(cur):
        nonlocal path, extra_moves
        for direction, (dx, dy) in directions:
            moved = False
            while True:
                next_pos = (cur[0] + dx, cur[1] + dy)

                # 다음 위치가 유효하지 않으면 탈출
                if not is_valid(next_pos):
                    break

                prev_dist = distance(cur, end)
                next_dist = distance(next_pos, end)

                # 최적 경로를 따르지 않는다면, 정크 무빙 기회가 없으면 중단
                if next_dist > prev_dist and extra_moves <= 0:
                    break

                # 정크 무빙이라면, 기회 차감
                if next_dist > prev_dist:
                    extra_moves -= 1

                moved = True
                path += direction
                cur = next_pos

                # 남은 거리 확인 (정확히 k만큼 이동해야 함)
                remaining_moves = (k - len(path)) - distance(cur, end)
                if remaining_moves != 0 and direction in ["r", "u"]:
                    break

            if moved:
                return cur
        return cur

    while len(path) < k:
        current = move(current)

    return path