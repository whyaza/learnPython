#!/usr/bin/python
# encoding: utf-8

import sys, re
from handlers import *
from util import *
from rules import *

class Parser:
    """
    解析器父类
    """
    def __init__(self, handler):
        self.handler = handler
        self.rules = []
        self.filters = []

    def addRule(self, rule):
        """
        添加规则
        """
        self.rules.append(rule)

    def addFilter(self, pattern, name):
        """
        添加过滤器
        """
        def filter(block, handler):
            return re.sub(pattern, handler.sub(name), block)
        self.filters.append(filter)

    def parse(self, file):
        """
        解析
        """
        self.handler.start('document')
        for block in blocks(file):
            for filter in self.filters:
                block = filter(block, self.handler)
            for rule in self.rules:
                if rule.condition(block):
                    last = rule.action(block, self.handler)
                    if last: break
        self.handler.end('document')

class BasicTextParser(Parser):
    """
    纯文本解析器
    """
    def __init__(self, handler):
        Parser.__init__(self, handler)
        self.addRule(ListRule())
        self.addRule(ListItemRule())
        self.addRule(TitleRule())
        self.addRule(HeadingRule())
        self.addRule(ParagraphRule())

        self.addFilter(r'\*(.+?)\*', 'emphasis')
        self.addFilter(r'(http://[\.a-zA-Z/]+)', 'url')
        self.addFilter(r'([\.a-zA-Z]+@[\.a-zA-Z]+[a-zA-Z]+)', 'mail')

"""
运行程序
"""
handler = HTMLRenderer()
parser = BasicTextParser(handler)
parser.parse(sys.stdin)
