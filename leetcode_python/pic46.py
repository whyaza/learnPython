def move(x,y):
    rs = x << 8
    rs += y
    return rs

print('0x{:x}'.format(move(0x12,0xd1)))
