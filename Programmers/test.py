import curses
import math
import time

def draw_heart(stdscr, angle):
    stdscr.clear()
    height, width = stdscr.getmaxyx()
    center_x, center_y = width // 2, height // 2

    for y in range(-15, 15):
        for x in range(-30, 30):
            # 기본 하트 방정식
            heart = (x**2 + y**2 - 1)**3 - x**2 * y**3
            
            # 회전 변환 적용
            x_rot = x * math.cos(angle) - y * math.sin(angle)
            y_rot = x * math.sin(angle) + y * math.cos(angle)
            
            if heart < 0:
                screen_x = int(center_x + x_rot * 2)  # 가로로 늘리기
                screen_y = int(center_y - y_rot)
                if 0 <= screen_x < width and 0 <= screen_y < height:
                    stdscr.addch(screen_y, screen_x, "*")
    
    stdscr.refresh()

def main(stdscr):
    curses.curs_set(0)
    angle = 0

    while True:
        draw_heart(stdscr, angle)
        angle += math.pi / 60  # 회전 속도
        time.sleep(0.05)

if __name__ == "__main__":
    curses.wrapper(main)
