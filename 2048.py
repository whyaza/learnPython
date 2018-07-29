#!/usr/bin python3

import curses
from random import randrange, choice
from collections import defaultdict

#用户行为与键盘的对应
actions = ['Up','Left','Down','Right','Restart','Exit']
letter_codes = [ord(ch) for ch in 'WASDRQwasdrq']
actions_dict = dict( zip(letter_codes, actions *2))

def get_user_action(keyboard) :
    #用户输入处理
    char = "N"
    while char not in actions_dict :
        char = keyboard.getch()
    return actions_dict[char]

def spawn(self):
    new_element = 4 if randrange(100) > 89 else 2
    


#矩阵转置

#矩阵逆转

#初始化棋盘
class GameField(object):
    def __init__(self, height=4,width=4,win=2048):
        self.height = height
        self.width = width
        self.win_value = win
        self.score = 0  #当前分数
        self.highscore = 0 #最高分
        self.reset()      #期盼重置
    #矩阵转置
    def transpose(field):
        return [list(row) for row in zip(*field)]
    #矩阵逆转
    def invert(field) :
        return [row[::-1] for row in field]
    #重置棋盘
    def reset(self): 
        if self.score > self.highscore :
            self.highscore = self.score
        self.score = 0
        self.field = [[0 for i in range(self.width)] for j in range(self.height) ]
        self.spawn()
        self.spawn()
    #随机生成一个2或者4
    def spawn(self):
        new_element = 4 if randrange(100) > 89 else 2
        (i ,j) = choice( [ (i,j) for i in range(self.width) for j in range(self.height) if self.field[i][j] ==0] )
        self.field[i][j] = new_element

    #def move_row_left(row):
     #   def tighten(row) : #把零散的非零单元挤到一块
      #      new_row = [i for i in row if i != 0]
       #     new_row += [0 for i in range]
    


def main 
