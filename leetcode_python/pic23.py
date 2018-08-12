#:打印菱形

for col in range(1,5):
    colnum = 2*col - 1
    spacenum = 4 - col
    print(' '*spacenum,end='')
    print('*'*colnum,end='')
    print(' '*spacenum,end='')
    print('')

for col in range(1,4):
    spacenum = col
    colnum = 7 - 2 * col
    print(' '*spacenum,end='')
    print('*'*colnum,end='')
    print(' '*spacenum,end='')
    print('')

