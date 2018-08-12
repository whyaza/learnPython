import curses
import time
import os
import random
stdscr = curses.initscr()
curses.noecho()     #不输出- -
curses.cbreak()     #立刻读取:暂不清楚- -
stdscr.keypad(1)    #开启keypad
stdscr.box()

width = os.get_terminal_size().columns
height = os.get_terminal_size().lines
c_y = height//2 - 1
c_x = width//2 - 10
stdscr.addstr(c_y+5,c_x,'press C to continue',curses.A_REVERSE)
while True:
    c = stdscr.getch()
    if c == ord('c') or c == ord('C'):
        break

zh_ = '1234567890-qwertyuiopasdfghjklzxcvbnm,[;l,]/~!@#$%^&*()_+}"?{:><}"'';'
while True:
    for linei in range(1,width-1):
        for linej in range(1,height-1):
            if linej == c_y:
                if linei <= 5 or linei+6 >= width:
                    stdscr.addstr(linej,linei,'$')
                else:
                    stdscr.addstr(linej,c_x,time.strftime('%Y-%m-%d %H:%M:%S'),curses.A_BOLD)
            else:
                randominx = random.randint(0,len(zh_)-1)
                stdscr.addstr(linej,linei,zh_[randominx])
    stdscr.move(c_y,c_x)
    stdscr.refresh()
    time.sleep(1)

curses.endwin()
