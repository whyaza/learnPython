import time, curses
import random
import os
import copy

cells = []
HEIGHT = os.get_terminal_size().lines
WIDTH = os.get_terminal_size().columns
models = 1 #默认模式1
speed = 0.1 #默认速度0.1

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

def randomcells():
    global cells
    ro = random.randint(1,100)
    #print(HEIGHT)
    #print(WIDTH)
    for i in range(20,HEIGHT - 20):
        for j in range(20,WIDTH - 20):
            if ro < 50 :
                cells.append([i,j,True])
                stdscr.addstr(i,j,'@')
            ro = random.randint(1,100)
    
    stdscr.refresh()

def draw():
    stdscr.erase()
    stdscr.refresh()
    try :
        for cell in cells:
            stdscr.addstr(cell[0],cell[1],'@')
        back_info = '      按b，回到主菜单'
        stdscr.addstr(HEIGHT-5,WIDTH-5,back_info,curses.A_BOLD)
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
        c = stdscr.getch()
        if c == ord('b'):
            return 
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
        time.sleep(speed)

def main(stdscr):
    global cells,models,speed
    while True:
        curses.noecho()
        curses.cbreak()
        stdscr.keypad(1)
        stdscr.box()
        stdscr.addstr(10,10,info,curses.A_BOLD)

        stdscr.nodelay(0)
        c = stdscr.getch()
        if c == ord('1'):
            models = 1
            speed = 0.1
        if c == ord('2'):
            models = 2
            speed = 0.5

        cells = []
        stdscr.erase()
        stdscr.move(HEIGHT//2,WIDTH//2)
        #设定两种模式，自动模式和自定义模式：
        if models == 1:   #开始自动模式
            randomcells()    
        if models == 2:
            init()
        stdscr.nodelay(1)
        play()
        stdscr.erase()


info = '''
                                                                            细胞自动机游戏说明:
                                                            1.按1/2键选择模式,１:自动模式,2:自定义模式
                                                            2.自定义模式下:键盘上下左右控制光标移动,空格设置初始细胞,o/O键开始启动细胞自动机
                                                            3.细胞自动机如果细胞移动出屏幕 or len(细胞) == 0时刻,会自动关闭
                                                                            祝您玩的愉快!~
'''

stdscr = curses.initscr()
stdscr.move(HEIGHT//2,WIDTH//2)
curses.wrapper(main)
