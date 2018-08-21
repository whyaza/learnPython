import time,curses,random,threading

pos = {
    'UP': (-1,0),
    'DOWN':(+1,0),
    'LEFT':(0,-1),
    'RIGHT':(0,+1),
}
current = 'RIGHT'
snake = [[1,1],[1,2],[1,3],[1,4],[1,5]]   #ex: [[1,1],[1,2],[1,3]]  [y,x]
head = snake[-1]
snake_speed = 0.1
rany, ranx = -1, -1

def isover(head):
    if snake.count(head) > 1:  #碰到自己身体
        return True
    if (head[0] == y-1) or (head[1] == x-1) or (head[0] == 0) or (head[1] == 0):    #碰到墙
        return True
    return False

def randomyx():
    global rany,ranx
    ranflag = False
    while ranflag is False:
        rany, ranx = random.randint(1,y-2) , random.randint(1,x-2)
        if [rany,ranx] not in snake:
            ranflag = True

def draw():
    stdscr.erase()
    stdscr.border()
    for si in snake:
        stdscr.addstr(si[0],si[1],'@',curses.color_pair(2))
    stdscr.addstr(rany,ranx,' ',curses.color_pair(1))
    stdscr.refresh()

def listening(head):
    global current
    while True:
        c = stdscr.getch()
        if c == curses.KEY_UP and current != 'DOWN':
            current = 'UP'
        elif c == curses.KEY_DOWN and current != 'UP':
            current = 'DOWN'
        elif c == curses.KEY_LEFT and current != 'RIGHT':
            current = 'LEFT'
        elif c == curses.KEY_RIGHT and current != 'LEFT':
            current = 'RIGHT'

def loop(stdscr):
    global head,snake_speed
    randomyx()    
    t1 = threading.Thread(target=listening, args=(head,), name='listenkeyboard')
    t1.start()
    while isover(head) is False:
        draw()
        head = [ head[0] + pos[current][0] , head[1] + pos[current][1]] 
        snake.append(head)
        if head[0] == rany and head[1] == ranx:
            randomyx()
            snake_speed = snake_speed - 0.01
        else:
            snake.pop(0)
        time.sleep(snake_speed)

stdscr = curses.initscr()
curses.noecho()     #不输出- -
curses.cbreak()     #立刻读取:暂不清楚- -
curses.start_color()  #开启颜色
curses.init_pair(1, curses.COLOR_RED, curses.COLOR_RED)#定义点的颜色
curses.init_pair(2, curses.COLOR_BLUE, curses.COLOR_BLUE) #定义蛇的颜色
#init_pair(n,f,b)修改颜色对n，让f为前景色，b为背景色。颜色对0天生的黑白色，不允许改。
stdscr.keypad(1)    #开启keypad
stdscr.border()
curses.curs_set(0)
(y,x) = stdscr.getmaxyx()
curses.wrapper(loop)
curses.endwin()
