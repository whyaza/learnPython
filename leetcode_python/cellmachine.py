import time, curses
import random
import os
import copy

cells = []
HEIGHT = os.get_terminal_size().lines
WIDTH = os.get_terminal_size().columns
class OuterScreenException(Exception):
    pass

def init():
    while True:
        c = stdscr.getch()
        (y,x) = stdscr.getyx()
        if c == ord('O') or c == ord('o'):
            break
        elif c == ord(' '):
            if [y,x,True] not in cells: #禁止重复添加
                cells.append([y,x,True])
                stdscr.addstr(y,x,'@')
        elif c == curses.KEY_UP:
            stdscr.move(y-1,x)
        elif c == curses.KEY_LEFT:
            stdscr.move(y,x-1)
        elif c == curses.KEY_DOWN:
            stdscr.move(y+1,x)
        elif c == curses.KEY_RIGHT:
            stdscr.move(y,x+1)

def draw():
    stdscr.erase()
    stdscr.refresh()
    try :
        for cell in cells:
            stdscr.addstr(cell[0],cell[1],'@')
        stdscr.refresh()
    except :
        raise OuterScreenException

def play():
    #设定规则:
#     每个细胞有两种状态 - 存活或死亡，每个细胞与以自身为中心的周围八格细胞产生互动。（如图，黑色为存活，白色为死亡）
    # 当前细胞为存活状态时，当周围低于2个（不包含2个）存活细胞时， 该细胞变成死亡状态。（模拟生命数量稀少）
    # 当前细胞为存活状态时，当周围有2个或3个存活细胞时， 该细胞保持原样。
    # 当前细胞为存活状态时，当周围有3个以上的存活细胞时，该细胞变成死亡状态。（模拟生命数量过多）
    # 当前细胞为死亡状态时，当周围有3个存活细胞时，该细胞变成存活状态。 （模拟繁殖）
    poss = ((-1,-1),(0,-1),(1,-1),(-1,0),(1,0),(-1,1),(0,1),(1,1))
    global cells
    while len(cells):
        
        for ls in range(len(cells)):
            for pos in poss:
                tempx = cells[ls][1] + pos[0]
                tempy = cells[ls][0] + pos[1]
                if ([tempy,tempx,True] not in cells) and ([tempy,tempx,False] not in cells):
                    cells.append( [tempy,tempx,False] )

        temp_cells = []
        for cell in cells:
            nearcs = 0
            for pos in poss:
                tempx = cell[1] + pos[0]
                tempy = cell[0] + pos[1]
                if [tempy,tempx,True] in cells: #周围的细胞还活着
                    nearcs += 1
            if cell[2] == True:   #该细胞为存活状态
                if nearcs < 2:
                    pass
                elif nearcs == 2 or nearcs == 3:
                    temp_cells.append( [cell[0],cell[1],True] )
                elif nearcs > 3:
                    pass
            else:   #细胞为死亡状态
                if nearcs == 3:
                    temp_cells.append( [cell[0],cell[1],True] )
        
        #for cell in temp_cells:
        #    print(cell[0],cell[1],cell[2])
        
        cells = copy.copy(temp_cells) 
        try:
            draw()
        except OuterScreenException as e:
            return
        time.sleep(1)
        
def main(stdscr):
    global cells
    while True:
        cells = []
        stdscr.erase()
        stdscr.move(HEIGHT//2,WIDTH//2)
        init()
        play()

info = '''
            细胞自动机游戏说明:
            1.按b/B键开始游戏,
            2.键盘上下左右控制光标移动,空格设置初始细胞,o/O键开始启动细胞自动机
            3.细胞自动机如果细胞移动出屏幕 or len(细胞) == 0时刻,会自动关闭
            4.祝您玩的愉快!~
'''

stdscr = curses.initscr()
curses.noecho()
curses.cbreak()
stdscr.keypad(1)
stdscr.box()
stdscr.addstr(10,10,info,curses.A_BOLD)
while True:
    c = stdscr.getch()
    if c == ord('B') or c == ord('b'):
        break
stdscr.erase()
stdscr.move(HEIGHT//2,WIDTH//2)
curses.wrapper(main)




