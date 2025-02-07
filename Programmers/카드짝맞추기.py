import collections
import functools

def solution(board, r, c):
    # 카드 간 최단 경로를 찾는 핵심 함수
    def firstRoute(r, c, tr, tc):
        # 행과 열 방향으로 최단 경로를 찾는 내부 함수들
        def goRow(r, c, tr):
            # 행 방향 이동 탐색
            visited = list(map(lambda _: False, range(4)))
            rq = collections.deque([])
            rq.append((r, 0))  # 시작 위치와 초기 깊이

            while rq and rq[0][0] != tr:
                curR, depth = rq.popleft()
                
                # 두 가지 이동 방식 탐색 (상하 방향)
                for dir in [1, -1]:
                    # 1. 인접한 칸으로 이동
                    if 0 <= curR + dir < 4 and not visited[curR + dir]:
                        visited[curR + dir] = True
                        rq.append((curR + dir, depth + 1))
                    
                    # 2. 연속된 빈 칸을 건너뛰며 이동
                    nr = curR
                    while 0 <= nr + dir < 4:
                        nr += dir
                        if board[nr][c] != 0:  # 카드를 만나면 정지
                            break
                    
                    # 새로운 위치 방문
                    if not visited[nr]:
                        visited[nr] = True
                        rq.append((nr, depth + 1))
            
            return rq[0][1]  # 최단 경로 깊이 반환

        # 열 방향 이동 탐색 (goRow와 유사한 로직)
        def goCol(c, r, tc):
            cq = collections.deque([])
            visited = list(map(lambda _: False, range(4)))
            cq.append((c, 0))
            
            while cq and cq[0][0] != tc:
                curC, depth = cq.popleft()
                
                for dir in [1, -1]:
                    # 1. 인접한 칸으로 이동
                    if 0 <= curC + dir < 4 and not visited[curC + dir]:
                        visited[curC + dir] = True
                        cq.append((curC + dir, depth + 1))
                    
                    # 2. 연속된 빈 칸을 건너뛰며 이동
                    nc = curC
                    while 0 <= nc + dir < 4:
                        nc += dir
                        if board[r][nc] != 0:  # 카드를 만나면 정지
                            break
                    
                    # 새로운 위치 방문
                    if not visited[nc]:
                        visited[nc] = True
                        cq.append((nc, depth + 1))
            
            return cq[0][1]  # 최단 경로 깊이 반환
        
        # 행 우선 vs 열 우선 경로 중 최단 경로 선택
        rowFirst = goRow(r, c, tr) + goCol(c, tr, tc)
        colFirst = goCol(c, r, tc) + goRow(r, tc, tr)
        return min(rowFirst, colFirst)
    
    # 보드의 최대 카드 번호 계산
    taskMax = max(list(functools.reduce(lambda x,y: x + y, board, [])))
    
    # 최소 이동 횟수 초기화 (큰 값으로 설정)
    answer = 100_000_000
    
    # 카드 방문 여부 추적 (이미 제거한 카드 번호는 True로 처리)
    taskVisited = list(map(lambda x: False, range(taskMax)))
    
    def dfs(r, c, depth, move):
        nonlocal board, answer, taskVisited
        
        # 모든 카드를 제거했다면 최소 이동 횟수 갱신
        if depth == taskMax:
            answer = min(move, answer)
            return 
        
        # 아직 제거하지 않은 카드 탐색
        for nextInd in range(taskMax):
            if taskVisited[nextInd]:
                continue
            
            # 현재 카드 방문 표시
            taskVisited[nextInd] = True
            next = nextInd + 1
            
            # 현재 카드의 두 위치 찾기
            np = []
            for row in range(4):
                for col in range(4):
                    if board[row][col] == next:
                        np.append((row, col))
            
            # 두 카드의 위치
            v0r, v0c, v1r, v1c = np[0][0], np[0][1], np[1][0], np[1][1]
            
            # 두 가지 카드 제거 순서 계산
            # 1. 첫 번째 카드 -> 두 번째 카드
            curMove0 = firstRoute(r, c, v0r, v0c) + firstRoute(v0r, v0c, v1r, v1c) + 2
            # 2. 두 번째 카드 -> 첫 번째 카드
            curMove1 = firstRoute(r, c, v1r, v1c) + firstRoute(v1r, v1c, v0r, v0c) + 2
            
            # 카드 제거 (보드에서 0으로 표시)
            board[v1r][v1c] = 0
            board[v0r][v0c] = 0
            
            # 더 짧은 경로로 재귀 탐색 (두 가지 경우 중 하나 선택)
            if curMove0 < curMove1:
                dfs(v1r, v1c, depth + 1, move + curMove0)
            else:
                dfs(v0r, v0c, depth + 1, move + curMove1)
            
            # 백트래킹: 카드 복원 및 방문 해제
            taskVisited[nextInd] = False
            board[v1r][v1c] = next
            board[v0r][v0c] = next
        
    # 초기 커서 위치에서 DFS 시작
    dfs(r, c, 0, 0)
    return answer
