import time, curses
import random
import os

LVD = 61.8

def init():
    cells = []
    width = os.get_terminal_size().columns
    height = os.get_terminal_size().lines
    for i in range(1,width-1):
        for j in range(1,height-1):
            if random.randint(1,100) >= LVD:
                y,x = range(1,width - 1) , range(1,height-1)
                if [y,x,True] not in cells:
                    cells.append([j,i,True])
                    stdscr.addstr(j,i,'@')
    # while True:
        # c = stdscr.getch()
        # (y,x) = stdscr.getyx()
        # if c == ord('o') or c == ord('O'):
            # break
        # elif c == ord(' '):
            # cells.append([y,x,True])
            # stdscr.addstr(y,x,'@')
        # elif c == curses.KEY_UP:
            # stdscr.move(y-1,x)
        # elif c == curses.KEY_LEFT:
            # stdscr.move(y,x-1)
        # elif c == curses.KEY_DOWN:
            # stdscr.move(y+1,x)
        # elif c == curses.KEY_RIGHT:
            # stdscr.move(y,x+1)
    return cells

def draw():
    for cell in cells:
        if cell[2] == True:
            stdscr.addstr(cell[0],cell[1],'@')
        else:
            stdscr.addstr(cell[0],cell[1],' ')
    stdscr.refresh()
    time.sleep(0.5)

def main(stdscr):
    #每个细胞有两种状态 - 存活或死亡，每个细胞与以自身为中心的周围八格细胞产生互动。（如图，黑色为存活，白色为死亡）
    #当前细胞为存活状态时，当周围低于2个（不包含2个）存活细胞时， 该细胞变成死亡状态。（模拟生命数量稀少）
    #当前细胞为存活状态时，当周围有2个或3个存活细胞时， 该细胞保持原样。
    #当前细胞为存活状态时，当周围有3个以上的存活细胞时，该细胞变成死亡状态。（模拟生命数量过多）
    #当前细胞为死亡状态时，当周围有3个存活细胞时，该细胞变成存活状态。 （模拟繁殖）
    #-> 0,1,4,5,6,7,8 :死亡  2:原样 3:原样
    near_pos = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]  #(y,x)
    while len(cells):
        for cell in cells:
            nearcs = 0
            for pos in near_pos:
                tempx = cell[0]+pos[0]
                tempy = cell[1]+pos[1]
                if [tempx,tempy,True] in cells:
                    nearcs += 1
            if cell[2] is True: #当前细胞为存活状态
                if nearcs < 2:
                    cell[2] = False
                elif 2 <= nearcs <= 3:
                    pass
                elif nearcs >= 4:
                    cell[2] = False
            else :  #当前细胞为死亡状态
                if nearcs == 3 or nearcs == 4 or nearcs == 2:
                    cell[2] = True
        draw()

stdscr = curses.initscr()
curses.noecho()
curses.cbreak()
stdscr.keypad(1)
stdscr.box()
stdscr.move(20,20)
cells = init()
curses.wrapper(main)




