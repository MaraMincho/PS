import sys
import collections

input = sys.stdin.readline
n = input() 
balls = list(map(str, input().strip()))

### 4가지 케이스
### 1. 빨간공을 왼족으로 몰기, 2. 빨간공을 오른쪽으로 몰기
### 3. 파란공을 왼쪽으로 몰기, 4. 파란공을 오른쪽으로 몰기

t = []

colors = ["R", "B"]
dirs = ["L", "R"]

for color in colors:
    for dir in dirs:
        curBalls = collections.deque(balls)
        if dir == "L":
            # Count how many of the color are at the left
            while curBalls and curBalls[0] == color:
                curBalls.popleft()
        else:
            # Count how many of the color are at the right
            while curBalls and curBalls[-1] == color:
                curBalls.pop()

        curT = len([ball for ball in curBalls if ball == color])
        t.append(curT)
print(min(t))