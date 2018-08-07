#!/usr/bin/python
# encoding: utf-8

def lines(file):
    """
    生成器,在文本最后加一空行
    """
    for line in file: yield line
    yield '\n'

def blocks(file):
    """
    生成器,生成单独的文本块
    """
    block = []
    for line in lines(file):
        if line.strip():
            block.append(line)
        elif block:
            yield ''.join(block).strip()
            block = []
